"""
Weapon.py
NewScript
"""


class Weapon:
	def __init__(self, name, recipe, type, speed, accuracy, damage, range, has_scope, rarity):
		self.name = name
		self.recipe = recipe
		self.type = type
		self.speed = speed
		self.accuracy = accuracy
		self.damage = damage
		self.range = range
		self.has_scope = has_scope
		self.rarity = rarity
		
		## Plural:
		if name [-1] in ["s","x","z"] or name [-2:] in ["ss","sh","ch"]:
			  self.plural = name + "es"
		elif name [-1] == "y": self.plural = name [:-1] + "ies"
		else: self.plural = name + "s"
