class User():
	"""Class containing information about user"""
	def __init__(self, first_name, last_name, login, sex, age):
		"""Initialization of attributes"""
		self.first_name = first_name
		self.last_name = last_name
		self.login = login
		self.sex = sex
		self.age = age

	def describe_user(self):
		print(f"\nInformację o użytkowniku: {self.login}:")
		print(f"\tImię: {self.first_name.title()}")
		print(f"\tNazwisko: {self.last_name.title()}")
		print(f"\tPłeć: {self.sex}")
		print(f"\tWiek: {self.age}")

	def greet_user(self):
		print(f"Witaj! {self.first_name.title()} {self.last_name.title()}.")

user_1 = User('łukasz', 'drozd', 'drozdzu88', 'male', 32)
user_2 = User('kamil', 'drozd', 'luckyluke88', 'male', 10)

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()