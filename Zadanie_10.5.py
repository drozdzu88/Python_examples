filename = 'D:/Lukasz/Kodowanie/python_projects/pliki_tekstowe/why_programming.txt'

with open(filename, 'a') as file_object: 

	while True:

		name = input('Jak się nazywasz? ')
		name = name.title()

		question = input(f'{name} dlaczego lubisz programowanie? ')
		file_object.write(f"Użytkownik {name} lubi programować ponieważ: \n\t{question}\n")
		message = input("Jeżeli chcesz wyjść wpisz 'tak':  ").lower()

		if message == 'tak':
			break
		else: 
			continue
