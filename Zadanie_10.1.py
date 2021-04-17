filename = 'D:/Lukasz/Kodowanie/python_projects/pliki_tekstowe/learning_python.txt'

with open(filename) as file_object:
	contents = file_object.read()

print(contents)

with open(filename) as file_object2:
	for line in file_object2:
		print(line.rstrip())

with open(filename) as file_object3:
	lines = file_object3.readlines()

for line in lines:
	print(line.rstrip())
