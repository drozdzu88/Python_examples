filename = 'D:/Lukasz/Kodowanie/python_projects/pliki_tekstowe/guest.txt'

with open(filename, 'w') as file_object: 
	file_object.write(input('Jak masz na imię ? '))