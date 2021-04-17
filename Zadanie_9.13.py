"""
Creating a class that rolling a dice
"""

from random import randint


class Die():
	""" Creatin a Die class """

	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self):
		"""rolling a die and get random number for 1 to number of sides"""
		random = randint(1,self.sides)
		print(random)

roll_1 = Die()
roll_1.roll_die()
roll_1.roll_die()
roll_1.roll_die()
roll_1.roll_die()
roll_1.roll_die()
roll_1.roll_die()
roll_1.roll_die()
roll_1.roll_die()
roll_1.roll_die()
roll_1.roll_die()

roll_2 = Die(10)
roll_2.roll_die()
roll_2.roll_die()
roll_2.roll_die()
roll_2.roll_die()
roll_2.roll_die()
roll_2.roll_die()
roll_2.roll_die()
roll_2.roll_die()
roll_2.roll_die()
roll_2.roll_die()

roll_3 = Die(20)
roll_3.roll_die()
roll_3.roll_die()
roll_3.roll_die()
roll_3.roll_die()
roll_3.roll_die()
roll_3.roll_die()
roll_3.roll_die()
roll_3.roll_die()
roll_3.roll_die()
roll_3.roll_die()



