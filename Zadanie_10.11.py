def get_my_num():
	"""Program zapisujący ulubioną liczbę użytkownika"""

	import json
	filename = 'fav_num.json'
	fav_num = input("Podaj swoją ulubioną liczbę: ")

	
	with open(filename, 'w', encoding='utf8') as f:
		json.dump(fav_num, f)

	
	return fav_num


def show_my_num():
	"""Program wyświetlający ulubioną liczbę"""

	import json
	filename = 'fav_num.json'

	try:
		with open(filename, encoding='utf8') as f:
			fav_num = json.load(f)
			

	except FileNotFoundError:
		fav_num = get_my_num()

	print(f"Twoja ulubiona liczba to {fav_num}")


show_my_num()


