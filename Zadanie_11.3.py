import unittest
from employee import Employee 

class TestEmployee(unittest.TestCase):
	"""Test kla dlasy Employee"""

	def setUp(self):
		"""Utworzenie egzemplarza pracownika do użycia we wszystkich metodach"""
		self.employer = Employee('Jan', 'Kowalski', 60000)
			

	def test_give_default_raise(self):
		"""Sprawdzenie wartości rocznej pensji z domyślną podwyżką"""

		self.employer.give_raise()
		self.employer.year_salary+=self.employer.given_raise
		self.assertEqual(self.employer.year_salary, 65000)

	
	def test_give_custom_raise(self):
		"""Sprawdzenie wartości rocznej pensji z indywidualną podwyżką"""

		self.employer.give_raise()
		self.employer.year_salary+=self.employer.given_raise
		self.assertEqual(self.employer.year_salary, 70000)



if __name__ == '__main__':
	unittest.main()