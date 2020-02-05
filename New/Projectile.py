"""
Projectile.py
NewScript
"""


class Projectile:
	def __init__(self, name, recipe, launcher, damage, rarity):
		self.name = name
		self.recipe = recipe
		self.damage = damage
		self.launcher = launcher
		self.rarity = rarity
		
		## Plural:
		if name [-1] in ["s","x","z"] or name [-2:] in ["ss","sh","ch"]:
			  self.plural = name + "es"
		elif name [-1] == "y": self.plural = name [:-1] + "ies"
		else: self.plural = name + "s"
