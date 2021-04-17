sandwich_orders = ['texas', 'podlaska', 'alabama', 'warszawska']
finished_sandwiches = []

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print(f"Przygotowano kanapkę {sandwich.title()}")

	finished_sandwiches.append(sandwich)

print("\nLista przygotowanych kanapek:")
for sandwich in finished_sandwiches:
	print(sandwich.title())