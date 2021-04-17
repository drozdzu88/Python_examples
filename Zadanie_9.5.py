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

user_1 = User('łukasz', 'drozd', 'drozdzu88', 'male', 32)


user_1.describe_user()
user_1.greet_user()

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.show_login_attempts()
user_1.reset_login_attempts()
user_1.show_login_attempts()