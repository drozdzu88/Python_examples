

def file_open(filename):
	"""funkcja otwierająca i wyświetlająca plik .txt"""
	try:
		with open(filename, encoding='utf-8') as file_object:
			contents = file_object.read()
			print(f"\nWyświetlamy zawartość pliku: \n{contents.title()}")
	except FileNotFoundError as e:
		#print(f"Przepraszamy, podany plik nie istnieje {e}")
		pass



filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
	file_open(filename)