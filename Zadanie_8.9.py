#Zdefiniowanie funckji do wyświetlania komunikatów 
def show_messages(messeages):
	for message in messeages:
		print(message)

#Podanie listy krótkich komunikatów
messeages = ['Cześć', 'Witaj', 'Siema', 'Czołem', 'Hej', 'Hejka']

#Wywołanie funkcji
show_messages(messeages)