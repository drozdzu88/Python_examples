#Definicja funkcji
def make_album(author_name, album_title, track_no=None ):
	"""Tworzenie słownika z nazwą wykonawcy i albumu"""
	album_info = {'author': author_name.title(), 'title': album_title,}
	
	if track_no:
		album_info['tracks_number'] = track_no
	return album_info

#Pętla dodające pozycje do słownika
while True:
	print("\nPodaj informację dotyczące płyty")
	
	print("Jeżeli chcesz opuścić program wpisz 'q'.")
	a_name = input("Podaj nazwę wykonawcy: ")
	if a_name == 'q':
		break

	print("Jeżeli chcesz opuścić program wpisz 'q'.")
	a_title = input("Podaj nazwę płyty: ")
	if a_title == 'q':
		break

	print("Jeżeli chcesz opuścić program wpisz 'q'.")
	t_n = input("Podaj liczbę utworów na płycie: ")
	if t_n == 'q':
		break
	#Wyświetlanie słownika
	album_inf = make_album(a_name, a_title, t_n )
	print(album_inf)



