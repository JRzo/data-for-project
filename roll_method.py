from random import randint

class Die:
	""" This method will act as D6 Die"""
	def __init__(self,num_side=6):
		""" The number of sides """
		self.num_sides = num_side

	def roll(self):
		""" This method will act as rolling the dice"""
		roll_d = randint(1,self.num_sides)