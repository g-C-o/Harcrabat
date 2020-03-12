"""
Animal.py
Harcrabat
"""

from Database import ANIMAL_HEALTH



class Animal:


	def __init__(self, type, name):

		self.name = name
		self.type = type
		self.panicked = False
		self.health = ANIMAL_HEALTH

		if type == "Chicken":
			self.meat = "Chicken Chunk"
		elif type == "Rabbit":
			self.meat = "Rabbit Chunk"
		elif type == "Cow":
			self.meat = "Beef Chunk"
		elif type == "Fish":
			self.meat = "Fish Chunk"
		elif type == "Sheep":
			self.meat = "Mutton Chunk"



class Chicken(Animal):
	

	def __init__(self, name, *args, **kwargs):
		
		self.type = "Chicken"

		Animal.__init__(type, *args, **kwargs)



class Rabbit(Animal):
	

	def __init__(self, name, *args, **kwargs):
		
		self.type = "Rabbit"

		Animal.__init__(type, *args, **kwargs)



class Cow(Animal):
	

	def __init__(self, name, *args, **kwargs):
		
		self.type = "Cow"

		Animal.__init__(type, *args, **kwargs)



class Fish(Animal):
	

	def __init__(self, name, *args, **kwargs):
		
		self.type = "Fish"

		Animal.__init__(type, *args, **kwargs)



class Sheep(Animal):
	

	def __init__(self, name, *args, **kwargs):
		
		self.type = "Sheep"

		Animal.__init__(type, *args, **kwargs)