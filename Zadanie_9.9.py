class Car():
	"""Simple try reprezent a car"""

	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return elegant description of car"""
		long_name = f"\n{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		"""Show information about car mileage"""
		print(f"Ten samochód ma przejechane {self.odometer_reading} km.")

	def update_odometer(self, mileage):
		"""Assign a given value to the odometer of the car
		   The change will be undone if you try to reset the counter.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print('Nie można cofnąć licznika przebiegu samochodu!')

	def increment_odometer(self, kilometers):
		"""Increment the car odometer value by a given value"""
		if kilometers > 0:
			self.odometer_reading += kilometers
		else:
			print('Nie można cofnąć licznika przebiegu samochodu!')

class Battery():
	"""Prosta próba modelowania akumulatora samochodu"""
	def __init__(self, battery_size=75):
		"""Inicjalizacja atrybutów akumulatora."""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Wyświetla informację o wielkości akumulatora."""
		print(f"Ten samochód ma akumulator o pojemości {self.battery_size} kWh.")
	def get_range(self):
		"""Wyświetla informację o zasiegu samochodu na podstawie pojemności akumulatora"""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315

		print(f"Zasięg tego samochodu wynosi około {range} km, po pełnym naładowaniu akumulatora. ")
	
	def upgrate_battery(self):
		"""Checking battery volume and upgrate if needed"""
		if self.battery_size != 100:
			self.battery_size = 100
		


class ElectricCar(Car):
	"""We introduce characteristics electric cars"""

	def __init__(self, make, model, year):
		
		
		"""
		Inicjalizacja atrybutów klasy nadrzędnej.
		A następnie inicjalizacja atrybutów charakterystycznych
		dla samochodu elektrycznego
		"""
		super().__init__(make, model, year)
		self.battery = Battery()	
	




my_tesla = ElectricCar('tesla', 'mosel s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrate_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name()) 

my_new_car.update_odometer(45)
my_new_car.read_odometer()

my_new_car.update_odometer(30)
my_new_car.read_odometer()

my_used_car = Car('ford', 's-max', 2010)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(110000)
my_used_car.read_odometer()

my_used_car.increment_odometer(-100)
my_used_car.read_odometer()

