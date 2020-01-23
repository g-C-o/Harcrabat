"""
Item.py
NewScript
"""


class Item:
	def __init__(self, recipe):
		#### self.name = name
		self.recipe = recipe
		#### Add Rarity calculation:
		####	Average Resource rarity
		####	divided by number of resources?
