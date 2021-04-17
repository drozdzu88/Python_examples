def describe_city(cinty_name, city_country='Polska'):
	"""Funkcja opisująca należność miasta do kraju"""
	print(f"{cinty_name.title()}, lewży w {city_country.title()}.")

describe_city('warszawa')
describe_city('łęczna', 'polska')
describe_city(cinty_name='paryż', city_country='francja')