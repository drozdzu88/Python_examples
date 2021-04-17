filename = 'D:/Lukasz/Kodowanie/python_projects/pliki_tekstowe/guest_book.txt'

with open(filename, 'a') as file_object: 

	while True:
	
		name = input('Jak masz na imię ? ')
		print(f"Witaj {name.title()}.")
		file_object.write(f"Użytkownik {name.title()} odwiedził naszą stronę.\n")
		message = input("Jeżeli chcesz wyjść wpisz 'tak':  ").lower()

		if message == 'tak':
			break
		else: 
			continue
