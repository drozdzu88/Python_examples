table = input("Dzień dobry, dla jakiej liczby osób potrzebujesz stolik? ")
table = int(table)

if table > 8:
	print(f"Chwileczkę! Musimy przygotować stolik dla {table} osób.")
else:
	print("Wasz stolik czeka na was. Proszę za mną!")