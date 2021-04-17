person_0 = {
	'first_name': 'łukasz', 
	'last_name': 'Drozd', 
	'age': 32, 
	'city': 'Mława',
}

person_1 = {
	'first_name': 'justyna',
	'last_name': 'Drozd',
	'age': 30,
	'city': 'Mława',
}

person_2 = {
	'first_name': 'róża',
	'last_name': 'Drozd',
	'age': 0,
	'city': 'Mława',
}

people = [person_0, person_1, person_2]

for person in people:
	if person['age'] > 1:
		print(f"Nazywam się:{person['first_name'].title()} {person['last_name'].title()} ")
		print(f"Mam: {person['age']} lata")
		print(f"Mieszkam w: {person['city']}")	
	else:
		print(f"Nazywam się:{person['first_name'].title()} {person['last_name'].title()} ")
		print(f"Mam: {person['age']} lat")
		print(f"Mieszkam w: {person['city']}")
