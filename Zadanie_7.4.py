prompt = "Proszę podaj swoje dodatki do pizzy:"
prompt += "\nPo wpisaniu komendy 'koniec' program zakończy dodawanie dodaktów. "

toppings = True
while toppings:
	toppings = input(prompt)

	if toppings == 'koniec':
		toppings = False
	else:
		print(topping.title())