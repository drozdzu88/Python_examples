favorite_places = {
	'łukasz': ['Grecja', 'Wyspy Zielonego Przylądka', 'Turcja'],
	'justyna': ['Chorwacja', 'Wyspy Zielonego Przylądka', 'Zambia'],
	'paweł': ['Maroko', 'Kuba', 'Meksyk'],
}

for name, places in favorite_places.items():
	print(f"\nUlubionymi mijescami {name.title()}, są: ")

	for place in places:
		print(f"\t{place}")