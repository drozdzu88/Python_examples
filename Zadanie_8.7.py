def make_album(author_name, album_title, track_no=None ):
	"""Tworzenie słownika z nazwą wykonawcy i albumu"""
	album_info = {'author': author_name.title(), 'title': album_title,}
	
	if track_no:
		album_info['tracks_number'] = track_no
	return album_info

album_inf = make_album('jimi hendrix', 'Electric Ladyland')
print(album_inf)

album_inf = make_album('dżem', 'Detox')
print(album_inf)

album_inf = make_album('dżem', 'Cegła')
print(album_inf)

album_inf = make_album('dżem', 'Najemnik', 7)
print(album_inf)
