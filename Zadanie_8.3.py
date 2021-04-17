def make_shirt(shirt_size, shirt_text):
	"""Informacje dotyczące zamówienia koszulki"""
	print(f"\nZamówiono koszulkę w rozmiarze: {shirt_size.upper()}.")
	print(f'Tekst na koszulce: "{shirt_text}"')

make_shirt('xl', 'Kocham Pythona!')
make_shirt(shirt_text='Czas na programowanie', shirt_size='l')