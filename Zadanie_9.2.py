class Restaurant():
	"""Class that models a restaurant"""

	def __init__(self, restaurant_name, cusine_type):
		self.restaurant_name = restaurant_name
		self.cusine_type = cusine_type

	def describe_restaurant(self):
		print(f"Restauracja {self.restaurant_name} serwuje kuchnię {self.cusine_type.title()}.")

	def open_restaurant(self):
		print(f"Restauracja {self.restaurant_name}. Otwarta jest w godzinach od 13 do 24.")

restaurant_1 = Restaurant('Piccolo', 'włoską')

restaurant_2 = Restaurant('Monari', 'polską')

restaurant_3 = Restaurant('KEI Shushi', 'japońską')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()