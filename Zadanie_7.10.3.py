responses = {}

repeat = ""

while repeat != 'nie':
	name = input("\nPodaj swoje imię: ")
	response = input("Gdzie byś pojechał na swoje wymażone wakacje? ")
	responses[name] = response

	repeat = input("Czy ktoś chce jeszcze wziąć udział w ankiecie ? (tak/nie)")
	

print("\n---Wyniki ankiety---")
for name, response in responses.items():
	print(f"{name.title()} chciałaby się wybrać do {response.title()}.")