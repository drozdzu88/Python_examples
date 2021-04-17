prompt = "Proszę podaj swoje dodatki do pizzy:"
prompt += "\nPo wpisaniu komendy 'koniec' program zakończy dodawanie dodaktów. "

toppings = ""
while toppings != 'koniec':
	toppings = input(prompt)

	if toppings != 'koniec':
		print(toppings)
		