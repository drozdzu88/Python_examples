def adding_num():
	"""Funkcja dodająca dwie liczby do siebie"""
	print("Podaj dwie liczby (a,b), które mają zostać dodane do siebie.")
	print("Wpisując 'q' zakończysz program.")

	while True:

		while True:
			num_a = input('Podaj pierwszą liczę: ')
			if num_a == 'q':
				return
			try:
				num_a = int(num_a)
				
			except ValueError:
				print("Podana wartość nie jest liczbą. Spróbuj jeszcze raz.")
				continue
			break

		while True:
			num_b = input('Podaj drugą liczbę: ')
			if num_b == 'q':
				return
			try:
				num_b = int(num_b)

			except ValueError:
				print("Podana wartość nie jest liczbą. Spróbuj jeszcze raz.")
				continue
			break

		sum = num_a+num_b
		print(sum)


adding = adding_num()
