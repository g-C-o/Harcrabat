"""
Resource.py
NewScript
"""

class Resource:
	def __init__(self, name, frequency, plural, reference):
		self.name = name
		self.plural = plural
		reference[self.name] = self
		reference[self.plural] = self
		if frequency <= 16: self.rarity = "Rare"
		elif frequency <= 80: self.rarity = "Uncommon"
		else: self.rarity = "Common"
		
		if name [-1] in ["s","x","z"] or name [-2:] in ["ss","sh","ch"]:
			   self.plural = name + "es"
		elif name [-1] == "y": self.plural = name [:-1] + "ies"
		else:
			   self.plural = name + "s"
