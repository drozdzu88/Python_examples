prompt = "Proszę podaj swoje dodatki do pizzy:"
prompt += "\nPo wpisaniu komendy 'koniec' program zakończy dodawanie dodaktów. "


while True:
	toppings = input(prompt)

	if toppings == 'koniec':
		break
	else:
		print(toppings.title())