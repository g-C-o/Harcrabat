"""
Resource.py
NewScript
"""

class Resource:
	def __init__(self, name, rarity):
		self.name = name
		self.rarity = rarity
		
		## Plural:
		if name [-1] in ["s","x","z"] or name [-2:] in ["ss","sh","ch"]:
			  self.plural = name + "es"
		elif name [-1] == "y": self.plural = name [:-1] + "ies"
		else: self.plural = name + "s"
