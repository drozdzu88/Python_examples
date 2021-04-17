def get_formatted_city(city, country, population=""):
	"""The functions formats the display data"""
	if population:
		displayed_data = f"{city.title()}, {country.title()} - populacja {population}"
	else: 
		displayed_data = f"{city.title()}, {country.title()}"
	return displayed_data