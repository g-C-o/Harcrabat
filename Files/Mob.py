"""
Mob.py
NewScript
"""


class Mob:
	def __init__(self, name, health, weapon, group_count, location, tier):
		self.name = name
		self.health = health
		self.weapon = hand_item
		self.group_count = group_count
		self.location = location
		self.tier = tier
		if tier == 1: self.rarity = "Common"
		elif tier == 2: self.rarity = "Uncommon"
		elif tier == 3: self.rarity = "Rare"
