def get_stored_username():
	"""Pobranie imienia z pliku o ile taki istnieje"""
	import json
	filename = 'username.json'
	try:
		with open(filename, encoding='utf8') as f:
			username = json.load(f)
	except FileNotFoundError as e:
		return None
	else:
		return username

def get_new_username():
	"""
	Proszenie użytkownika aby podał swoje imię, a następnie zapisanie tego imienia w pliku
	"""
	import json
	username = input("Podaj swoje imię: ")
	filename = 'username.json'
	with open(filename, 'w', encoding='utf8') as f:
		json.dump(username, f, ensure_ascii=False)
	return username


def check_name():
	"""Sprawdzenie czy poprzednie imie należy do nas"""
	username = get_stored_username()
	while True:
			answer =input(f"Czy Twoje imię to: {username.title()}? Wpisz ('tak'/'nie')").lower()
		
			if answer == 'tak':
				print(f"Witaj ponownie {username.title()}!")
				break
			elif answer == 'nie':
				username = get_new_username()
				print(f"Twoje imię zostało zapisane i zostanie użyte później, {username.title()}!")
				break
			else:
				print('wpisz tak lub nie.')
				continue

def greet_user():
	"""Przywitanie użytkownika z użyciem jego imienia"""

	username = get_stored_username()
	if username:
		loop = check_name()

	else: 
		username = get_new_username()
		print(f"Twoje imię zostało zapisane i zostanie użyte później, {username.title()}!")


greet_user()


	
	


