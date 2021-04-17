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

	#print(list1)
	return list1

lottery = drawing()
print(f"Wygrywający kutpon zawiera: \n\t{lottery}")