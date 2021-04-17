#Zdefiniowanie funckji do wyświetlania komunikatów 
def show_messages(messages):
	for message in messages:
		print(message)


#Funkcja przenosząca komunikaty na inną listę
def send_messages(messages, sent_messages):
	print("\nRozpoczęcie przenoszenia funkcji")
	while messages:
		current_message = messages.pop()
		print(f"Przenoszę wiadomość {current_message}")
		sent_messages.append(current_message)


#Podanie listy krótkich komunikatów
messages = ['Cześć', 'Witaj', 'Siema', 'Czołem', 'Hej', 'Hejka']
sent_messages = []

#Wywołanie funkcji
show_messages(messages)
send_messages(messages, sent_messages)

#Wyświetlenie list dla sprawdzenia poprawnosci programu
print(messages)
print(sent_messages)