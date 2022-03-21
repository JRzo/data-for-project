from random import choice

class RandomWalk:
	""" This class will store all of the intances of randomwalk"""
	def __init__(self,num_points=5000):
		""" Will keep everything stored""" 
		self.num_points = num_points

		# All walks starts at (0,0)
		self.x_value = [0]
		self.y_value = [0]

	def get_step(self,something):
		""" This will calculate and determine the direction"""
		# Decide  which direction to go and how far it will go
		self.steps = 0
		direction_x = choice([1,-1])
		distance_x = choice([0,1,2,3,4])

		direction_y = choice([1,-1])
		distance_y = choice([0,1,2,3,4])

		if something == 'x':
			self.steps = distance_x * direction_x
			return self.steps
			
		if something == 'y':
			self.steps == distance_y * direction_y
			return self.steps

	def fill_walk(self):
		""" To calculate all points of our walk"""

		# Keep taking steps until the walk reaches the desirble length
		while len(self.x_value) < self.num_points:
			x_step = self.get_step('x')
			y_step = self.get_step('y')

			if x_step == 0 and y_step == 0:
				continue

			# Calculating the new positive 
			x = self.x_value[-1] + x_step
			y = self.x_value[-1] + y_step

			self.x_value.append(x)
			self.y_value.append(y)