class Employee():
	"""Klasa zapisująca imię, nazwisko i wartość rocznych zarobkó pracownika"""

	def __init__(self, first_name, last_name, year_salary):
		"""Przechowuje informację o pracowniku"""
		self.first_name = first_name
		self.last_name = last_name
		self.year_salary = year_salary

	def give_raise(self, given_raise=5000):
		"""Metoda przydzielająca podwyżkę, domyślnie 5000 zł rocznie"""
		self.given_raise = given_raise
		self.year_salary += given_raise
		
		
		
	
	def show_new_salary(self):
		"""Wyświetlenie nowej rocznej pensji"""

		print(f"Wypłata wynosi: {self.year_salary} rocznie.")


