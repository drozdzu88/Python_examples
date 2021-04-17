def make_shirt(shirt_size='xl', shirt_text='Uwielbiam Pythona'):
	"""Informacje dotyczące zamówienia koszulki"""
	print(f"\nZamówiono koszulkę w rozmiarze: {shirt_size.upper()}.")
	print(f'Tekst na koszulce: "{shirt_text}"')

make_shirt()
make_shirt('l')
make_shirt('m', 'Hello World!')
make_shirt(shirt_size='s', shirt_text='Python > C#')