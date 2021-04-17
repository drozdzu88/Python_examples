"""we create a drawing machine"""

from random import choice 


def drawing(): 
	"""drawing an elements from list"""
	colection_of_elements = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 1, 2, 3, 4, 5]

	list1 = []
	

	for element in colection_of_elements:
		if len(list1) <= 3:
			element = choice(colection_of_elements)
			colection_of_elements.remove(element)
			list1.append(element)
		else:
			break

	
	return list1


def how_many_times():

	"""How many iterations are needed to repeat the result"""
	
	count = 1
	print(f"Mój kupon zawiera: \n\t{my_ticket}")

	while True:	

		ticket_2 = drawing()
		if ticket_2 == my_ticket:
			print(f"Kupon {ticket_2} został ponownie wylosowany po {count} iteracjach.")
			break
		else:
			count += 1
			

my_ticket = drawing()
print(f"Wygrywający kutpon zawiera: \n\t{my_ticket}")
print('\nSprawdźmy, za którym razem powtórzy się wynik z kuponu.')
ticket_2 = how_many_times()