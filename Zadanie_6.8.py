kot = {
	'pet_name': "kicia",
	'first_name': "justyna",
	'last_name': "drozd",
}

pies = {
	'pet_name': "burek",
	'first_name': "łukasz",
	'last_name': "drozd",
}

chomik = {
	'pet_name': "maxio",
	'first_name': "róża",
	'last_name': "drozd",
}

pets = [kot, pies, chomik]

for pet in pets:
	print(f"Imię pupila to: {pet['pet_name']}!")
	print(f"Imię i Nazwisko właściciela to: {pet['first_name'].title()} {pet['last_name'].title()}")