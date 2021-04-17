sandwich_orders = ['texas', 'podlaska', 'alabama', 'warszawska', 'podlaska', 'texas', 'podlaska', 'alabama']
finished_sandwiches = []

print("Niestety skończyły się nam składniki na kanapkę 'podlaska'")

while 'podlaska' in sandwich_orders:
	sandwich_orders.remove('podlaska')
print(sandwich_orders)

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print(f"Przygotowano kanapkę {sandwich.title()}")

	finished_sandwiches.append(sandwich)

print("\nLista przygotowanych kanapek:")
for sandwich in finished_sandwiches:
	print(sandwich.title())