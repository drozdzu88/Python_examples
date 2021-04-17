glosariusz = {
	'pętla': 'definicja 1',
	'for': 'definicja 2',
	'if': 'definicja 3',
	'lista': 'definicja 4',
	'biblioteka': 'definicja 5',
	'string': 'definicja 6',
	'liczba': 'definicja 7',
}

for key, value in glosariusz.items():
	print(f"{key.title()}: \n\t{value.title()}.")
