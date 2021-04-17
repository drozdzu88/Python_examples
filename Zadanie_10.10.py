
def count_word(filename):
	try:
		with open(filename, encoding = 'utf-8') as file_object:
			contents = file_object.read()
	except FileNotFoundError as f:
		print(f"Nie można odnaleźć pliku {filename}")
	else: 
		number = contents.lower().count('the ')
		print(f"Plik {filename} zawiera {number} słowa 'the'.")



filenames = ['D:\\Lukasz\\Kodowanie\\python_projects\\pliki_tekstowe\\alice.txt', 'D:\\Lukasz\\Kodowanie\\python_projects\\pliki_tekstowe\\little_women.txt', 'D:\\Lukasz\\Kodowanie\\python_projects\\pliki_tekstowe\\moby_dick.txt', 'D:\\Lukasz\\Kodowanie\\python_projects\\pliki_tekstowe\\siddhartha.txt']
for filename in filenames:
	count_word(filename)