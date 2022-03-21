from random import randint

class Die:
	""" Here will be a dice class"""
	def __init__(self,num_side=6):
		""" Assuming that the dice has 6 sides"""
		self.num_sides = num_side

	def roll(self):
		""" WIll roll the dice to each time"""
		return randint(1,self.num_sides)



