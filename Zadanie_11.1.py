import unittest
from city_functions import get_formatted_city

class CityTestCase(unittest.TestCase):
	"""Test dla programu 'city_function.py'"""

	def test_city_country(self):
		"""Czy dane w postaci 'Santiago, Chile' są obsługiwane dobrze"""
		formatted_city = get_formatted_city('santiago', 'chile')
		self.assertEqual(formatted_city, 'Santiago, Chile')

	def test_city_country_population(self):
		"""Czy dane w postaci 'Santiago, Chile - populacja 5000000' są obsługiwane dobrze"""
		formatted_city = get_formatted_city('santiago', 'chile', 5000000)
		self.assertEqual(formatted_city, 'Santiago, Chile - populacja 5000000')

if __name__ == '__main__':
	unittest.main()

