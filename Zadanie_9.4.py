class Restaurant():
	"""Class that models a restaurant"""

	def __init__(self, restaurant_name, cusine_type):
		self.restaurant_name = restaurant_name
		self.cusine_type = cusine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(f"Restauracja {self.restaurant_name} serwuje kuchnię {self.cusine_type.title()}.")

	def open_restaurant(self):
		print(f"Restauracja {self.restaurant_name}. Otwarta jest w godzinach od 13 do 24.")

	def set_number_served(self):
		"""Show how many clients were severd today"""
		print(f"Dzisiaj obsłużyliśmy {self.number_served} klientów!")

	def increment_number_served(self, clients):
		"""Add another served clients to number_served"""
		if clients > 0:
			self.number_served += clients
		else:
			print("Nie można obsłużyć ujemnej liczby klientów")



restaurant = Restaurant('Piccolo', 'włoską')



restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served()
restaurant.increment_number_served(4)
restaurant.set_number_served()
restaurant.increment_number_served(-2)
restaurant.set_number_served()