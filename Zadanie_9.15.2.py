import random

def drawing(): 
	"""drawing an elements from list"""
	return random.sample('abcdefghijk12345', 4)

def how_many_times(my_ticket):
    """How many iterations are needed to repeat the result"""
    print(f"Mój kupon zawiera: \n\t{my_ticket}")
    count = 1
    while drawing() != my_ticket:
        count += 1
    print(f"Kupon {my_ticket} został ponownie wylosowany po {count} iteracjach.")

ticket = drawing()
my_ticket = how_many_times(ticket)