def city_country(city_name, country_name):
	"""Funckja formatuje dane wejściowe do postaci 'Santiago, Chwile'"""
	formatted_info = f"{country_name}, {city_name}"
	return formatted_info.title()

#Wyświetlanie danych wyjściowych
record_data = city_country('warszawa', 'poland')
print(f"\n{record_data}")
record_data = city_country('paris', 'France')
print(f"\n{record_data}")
record_data = city_country('london', 'england')
print(f"\n{record_data}")


