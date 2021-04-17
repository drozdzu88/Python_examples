number = input("Podaj proszę dowolną liczbę: ")
number = int(number)

if number % 10 == 0:
	print(f"Liczba {number} jest podzielna przez 10")
else:
	print(f"Liczba {number} nie jest podzielna przez 10")