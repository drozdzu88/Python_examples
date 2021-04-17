#Funkcja wyświetlająca składniki kanapki
def sandwich(*args):
	print("\nLista składników dodana do kanapki:")
	for component in args:
		print(f"- {component}")

#Uruchomienie funkcji i wyświetlenie składników 
sandwich('żółty ser')
sandwich('żółty ser', 'pomidor')
sandwich('żółty ser', 'pomidor', 'bekon')
