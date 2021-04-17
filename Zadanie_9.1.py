class Restaurant():
	"""Class that models a restaurant"""

	def __init__(self, restaurant_name, cusine_type):
		self.restaurant_name = restaurant_name
		self.cusine_type = cusine_type

	def describe_restaurant(self):
		print(f"Restauracja {self.restaurant_name} serwuje kuchnię {self.cusine_type.title()}.")

	def open_restaurant(self):
		print(f"Restauracja {self.restaurant_name}. Otwarta jest w godzinach od 13 do 24.")

restaurant = Restaurant('Piccolo', 'włoską')

print(restaurant.restaurant_name)
print(restaurant.cusine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()