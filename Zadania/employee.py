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
		
		print(f"Czy kwota podwyżki ma być inna niż domyślna? ('t'/'n')")
				
		while True:
			answer = input("Odpowiedź: ")
			if answer == 'n':
				self.year_salary += given_raise
				break

			elif answer == 't':
				given_raise = input("Podaj kwotę podwyżki: ")
				try:
					given_raise =int(given_raise)
					
				except ValueError:
					print("Podaj wartość liczbową")
					continue
				else:
					self.year_salary += given_raise
					break

			else:
				print("Musisz wpisać 'n' lub 't' i określić wysokość podwyżki")
				continue
		
	
	def show_new_salary(self):
		"""Wyświetlenie nowej rocznej pensji"""

		print(f"Wypłata wynosi: {self.year_salary} rocznie.")


