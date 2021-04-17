filename = 'D:/Lukasz/Kodowanie/python_projects/pliki_tekstowe/learning_python.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	line = line.replace("Pythonie", "C")
	print(line.rstrip())