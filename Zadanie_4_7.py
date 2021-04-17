numbers = []
for value in range(3,30):
	qubic = value**3
	numbers.append(qubic)
print(numbers)


#Zadanie z apomocą listy skłądanej
numbers_1 =[value**3 for value in range(3,30)]
print(numbers_1)