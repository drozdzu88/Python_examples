prompt = "Podaj swój wiek:"
prompt += "\nPo wpisaniu 'koniec' wyjdziesz z programu. "

age = ""
while age != 'koniec':
	age = input(prompt)
	
	if age != 'koniec':
		age = int(age)

		if age < 3:
			print("Bilet jest bezpłatny")
		elif age < 12:
			print("Bilet kosztuje 10zł")
		else:
			print("Bilet kosztuje 15 zł")
	
