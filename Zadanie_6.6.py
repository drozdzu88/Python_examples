favorite_languages = {
	'janek': 'python',
	'sara': 'C',
	'edward': 'ruby',
	'paweł': 'python',
}

respondents = ['janek', 'kasia', 'edward', 'łukasz', 'agnieszka', 'justyna']

for person in respondents:

	if person in favorite_languages.keys():
		print(f"{person.title()}! Dziękujemy za udział w ankiecie.")
	else:
		print(f"{person.title()}! Zapraszamy do udziału w ankiecie.")