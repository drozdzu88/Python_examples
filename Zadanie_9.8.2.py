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
		self.privileges = Privileges(['może dodać posty', 'może edytować własne posty'])

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

	def has_privilege(self, name):
		return self.privileges.has_privilege(name)

class Privileges():
	"""Class containing information about privileges"""
	def __init__(self, privileges):
		self.privileges = privileges
	
	def show_privileges(self):
		"""Shows Admin privileges"""
		
		print(f"Jako Admin może: {self.privileges}.")

	def has_privilege(self, name):
		return name in self.privileges




class Admin(User):
	"""Class containing information about Admin"""
	def __init__(self, first_name, last_name, login, sex, age):
		"""
		Inicjalizacja atrybutów klasy nadrzędnej oraz atrybutów klasy Admin
		"""
		
		super().__init__(first_name, last_name, login, sex, age)
		self.privileges = Privileges(['może dodać posty', 'może usuwać posty', 'może zbanować użytkownika'])

	
	


user_0 = Admin('jan', 'kowalski', 'jkowal', 'male', 25,)
user_0.describe_user()
user_0.privileges.show_privileges()
user_0.greet_user()
print(user_0.has_privilege('może dodać posty'))

user_1 = User('paweł', 'nowak', 'pnow', 'male', 30)
user_1.describe_user()
user_1.privileges.show_privileges()
user_1.greet_user()
print(user_1.has_privilege('może usuwać posty'))

