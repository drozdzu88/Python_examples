class User():
	"""Class containing information about user"""
	def __init__(self, first_name, last_name, login, sex, age):
		"""Initialization of attributes"""
		self.first_name = first_name
		self.last_name = last_name
		self.login = login
		self.sex = sex
		self.age = age
		self.login_attempts = 0

	def describe_user(self):
		print(f"\nInformację o użytkowniku: {self.login}:")
		print(f"\tImię: {self.first_name.title()}")
		print(f"\tNazwisko: {self.last_name.title()}")
		print(f"\tPłeć: {self.sex}")
		print(f"\tWiek: {self.age}")

	def greet_user(self):
		print(f"Witaj! {self.first_name.title()} {self.last_name.title()}.")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

	def show_login_attempts(self):
		print(f"Logowałeś się {self.login_attempts} razy!")

class Privileges():
	"""Class containing information about privileges"""
	def __init__(self):
		self.privileges = ['może dodać posty', 'może usuwać posty', 'może zbanować użytkownika']
	def show_privileges(self):
		"""Shows Admin privileges"""
		
		print(f"Jako Admin może: {self.privileges[0]}, {self.privileges[1]}, {self.privileges[2]}.")




class Admin(User):
	"""Class containing information about Admin"""
	def __init__(self, first_name, last_name, login, sex, age):
		"""
		Inicjalizacja atrybutów klasy nadrzędnej oraz atrybutów klasy Admin
		"""
		
		super().__init__(first_name, last_name, login, sex, age)
		self.privileges = Privileges()

	
	


user_0 = Admin('jan', 'kowalski', 'jkowal', 'male', 25,)
user_0.describe_user()
user_0.privileges.show_privileges()
user_0.greet_user()

