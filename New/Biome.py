"""
Biome.py
Harcrabat
"""

from Database import BIOME_WEIGHTS, RESOURCE_WEIGHTS, HARVEST_SIZE
import Item
import Mob
import Animal
from random import choices 


class Biome:
	def __init__(self, type, preposition, primary_resource, secondary_resource, tertiary_resource, primary_mob, secondary_mob, tertiary_mob, animal, primary_loot, secondary_loot, rarity):
		self.type = type
		self.preposition = preposition
		self.pri_R = primary_resource
		self.sec_R = secondary_resource
		self.ter_R = tertiary_resource
		self.pri_M = primary_mob
		self.sec_M = secondary_mob
		self.ter_M = tertiary_mob
		self.animal = animal
		self.rarity = rarity

	def gen_resources(self):
		new_resources = choices([self.pri_R, self.sec_R, self.ter_R], weights=RESOURCE_WEIGHTS, k = HARVEST_SIZE)
		return new_resources



class Forest(Biome):


	def __init__(self, *args, **kwargs):
		
		self.type = "Forest"
		self.preposition = "into a"
		self.pri_R = Item.Wood
		self.sec_R = Item.Soil
		self.ter_R = Item.Soil
		self.pri_M = Mob.Fighter
		self.sec_M = Mob.Fighter
		self.ter_M = Mob.Fighter
		self.animal = Animal.Chicken
		self.rarity = "Common"

		Biome.__init__(type, preposition, pri_R, sec_R, ter_R, pri_M, sec_M, ter_M, animal, rarity, *args, **kwargs)



class Jungle(Biome):


	def __init__(self, *args, **kwargs):
		
		self.type = "Jungle"
		self.preposition = "into a"
		self.pri_R = Item.Wood
		self.sec_R = Item.Soil
		self.ter_R = Item.Emerald
		self.pri_M = Mob.Fighter
		self.sec_M = Mob.Fighter
		self.ter_M = Mob.Predator
		self.animal = Animal.Chicken
		self.rarity = "Uncommon"

		Biome.__init__(type, preposition, pri_R, sec_R, ter_R, pri_M, sec_M, ter_M, animal, rarity, *args, **kwargs)



class Grove(Biome):


	def __init__(self, *args, **kwargs):
		
		self.type = "Grove"
		self.preposition = "into a"
		self.pri_R = Item.Wood
		self.sec_R = Item.Fruit
		self.ter_R = Item.Emerald
		self.pri_M = Mob.Fighter
		self.sec_M = Mob.Predator
		self.ter_M = Mob.Fighter
		self.animal = Animal.Chicken
		self.rarity = "Rare"

		Biome.__init__(type, preposition, pri_R, sec_R, ter_R, pri_M, sec_M, ter_M, animal, rarity, *args, **kwargs)



class Garden(Biome):


	def __init__(self, *args, **kwargs):
		
		self.type = "Garden"
		self.preposition = "into a"
		self.pri_R = Item.Wood
		self.sec_R = Item.Emerald
		self.ter_R = Item.Gold
		self.pri_M = Mob.Fighter
		self.sec_M = Mob.Predator
		self.ter_M = Mob.Goblin
		self.animal = Animal.Chicken
		self.rarity = "Legendary"

		Biome.__init__(type, preposition, pri_R, sec_R, ter_R, pri_M, sec_M, ter_M, animal, rarity, *args, **kwargs)



class Desert(Biome):


	def __init__(self, *args, **kwargs):
		
		self.type = "Desert"
		self.preposition = "into a"
		self.pri_R = Item.Sand
		self.sec_R = Item.Stone
		self.ter_R = Item.Stone
		self.pri_M = Mob.Destroyer
		self.sec_M = Mob.Destroyer
		self.ter_M = Mob.Destroyer
		self.animal = Animal.Rabbit
		self.rarity = "Common"

		Biome.__init__(type, preposition, pri_R, sec_R, ter_R, pri_M, sec_M, ter_M, animal, rarity, *args, **kwargs)



class Tundra(Biome):


	def __init__(self, *args, **kwargs):
		
		self.type = "Tundra"
		self.preposition = "into a"
		self.pri_R = Item.Sand
		self.sec_R = Item.Stone
		self.ter_R = Item.Iron
		self.pri_M = Mob.Destroyer
		self.sec_M = Mob.Destroyer
		self.ter_M = Mob.Annihilator
		self.animal = Animal.Rabbit
		self.rarity = "Uncommon"

		Biome.__init__(type, preposition, pri_R, sec_R, ter_R, pri_M, sec_M, ter_M, animal, rarity, *args, **kwargs)



class Badland(Biome):


	def __init__(self, *args, **kwargs):
		
		self.type = "Badland"
		self.preposition = "into a"
		self.pri_R = Item.Sand
		self.sec_R = Item.Cacti
		self.ter_R = Item.Iron
		self.pri_M = Mob.Destroyer
		self.sec_M = Mob.Annihilator
		self.ter_M = Mob.Destroyer
		self.animal = Animal.Rabbit
		self.rarity = "Rare"

		Biome.__init__(type, preposition, pri_R, sec_R, ter_R, pri_M, sec_M, ter_M, animal, rarity, *args, **kwargs)



class Temple(Biome):


	def __init__(self, *args, **kwargs):
		
		self.type = "Temple"
		self.preposition = "into a"
		self.pri_R = Item.Sand
		self.sec_R = Item.Iron
		self.ter_R = Item.Diamond
		self.pri_M = Mob.Destroyer
		self.ter_M = Mob.Annihilator
		self.sec_M = Mob.Troll
		self.animal = Animal.Rabbit
		self.rarity = "Legendary"

		Biome.__init__(type, preposition, pri_R, sec_R, ter_R, pri_M, sec_M, ter_M, animal, rarity, *args, **kwargs)



class Prairie(Biome):


	def __init__(self, *args, **kwargs):
		
		self.type = "Prairie"
		self.preposition = "into a"
		self.pri_R = Item.Soil
		self.sec_R = Item.Water
		self.ter_R = Item.Water
		self.pri_M = Mob.Raider
		self.sec_M = Mob.Raider
		self.ter_M = Mob.Raider
		self.animal = Animal.Cow
		self.rarity = "Common"

		Biome.__init__(type, preposition, pri_R, sec_R, ter_R, pri_M, sec_M, ter_M, animal, rarity, *args, **kwargs)



class Meadow(Biome):


	def __init__(self, *args, **kwargs):
		
		self.type = "Meadow"
		self.preposition = "into a"
		self.pri_R = Item.Soil
		self.sec_R = Item.Water
		self.ter_R = Item.Diamond
		self.pri_M = Mob.Raider
		self.sec_M = Mob.Raider
		self.ter_M = Mob.Minion
		self.animal = Animal.Cow
		self.rarity = "Uncommon"

		Biome.__init__(type, preposition, pri_R, sec_R, ter_R, pri_M, sec_M, ter_M, animal, rarity, *args, **kwargs)



class Swamp(Biome):


	def __init__(self, *args, **kwargs):
		
		self.type = "Swamp"
		self.preposition = "into a"
		self.pri_R = Item.Soil
		self.sec_R = Item.Vine
		self.ter_R = Item.Diamond
		self.pri_M = Mob.Raider
		self.sec_M = Mob.Minion
		self.ter_M = Mob.Raider
		self.animal = Animal.Cow
		self.rarity = "Rare"

		Biome.__init__(type, preposition, pri_R, sec_R, ter_R, pri_M, sec_M, ter_M, animal, rarity, *args, **kwargs)



class Fort(Biome):


	def __init__(self, *args, **kwargs):
		
		self.type = "Fort"
		self.preposition = "into a"
		self.pri_R = Item.Soil
		self.sec_R = Item.Diamond
		self.ter_R = Item.Quartz
		self.pri_M = Mob.Raider
		self.sec_M = Mob.Minion
		self.ter_M = Mob.Zombie
		self.animal = Animal.Cow
		self.rarity = "Legendary"

		Biome.__init__(type, preposition, pri_R, sec_R, ter_R, pri_M, sec_M, ter_M, animal, rarity, *args, **kwargs)



class Lake(Biome):


	def __init__(self, *args, **kwargs):
		
		self.type = "Lake"
		self.preposition = "into a"
		self.pri_R = Item.Water
		self.sec_R = Item.Sand
		self.ter_R = Item.Sand
		self.pri_M = Mob.Defender
		self.sec_M = Mob.Defender
		self.ter_M = Mob.Defender
		self.animal = Animal.Fish
		self.rarity = "Common"

		Biome.__init__(type, preposition, pri_R, sec_R, ter_R, pri_M, sec_M, ter_M, animal, rarity, *args, **kwargs)



class Beach(Biome):


	def __init__(self, *args, **kwargs):
		
		self.type = "Beach"
		self.preposition = "into a"
		self.pri_R = Item.Water
		self.sec_R = Item.Sand
		self.ter_R = Item.Gold
		self.pri_M = Mob.Defender
		self.sec_M = Mob.Defender
		self.ter_M = Mob.Guardian
		self.animal = Animal.Fish
		self.rarity = "Uncommon"

		Biome.__init__(type, preposition, pri_R, sec_R, ter_R, pri_M, sec_M, ter_M, animal, rarity, *args, **kwargs)



class Island(Biome):


	def __init__(self, *args, **kwargs):
		
		self.type = "Island"
		self.preposition = "onto an"
		self.pri_R = Item.Water
		self.sec_R = Item.Bone
		self.ter_R = Item.Gold
		self.pri_M = Mob.Defender
		self.sec_M = Mob.Guardian
		self.ter_M = Mob.Defender
		self.animal = Animal.Fish
		self.rarity = "Rare"

		Biome.__init__(type, preposition, pri_R, sec_R, ter_R, pri_M, sec_M, ter_M, animal, rarity, *args, **kwargs)



class Shipwreck(Biome):


	def __init__(self, *args, **kwargs):
		
		self.type = "Shipwreck"
		self.preposition = "onto a"
		self.pri_R = Item.Water
		self.sec_R = Item.Gold
		self.ter_R = Item.Emerald
		self.pri_M = Mob.Defender
		self.sec_M = Mob.Guardian
		self.ter_M = Mob.Skeleton
		self.animal = Animal.Fish
		self.rarity = "Legendary"

		Biome.__init__(type, preposition, pri_R, sec_R, ter_R, pri_M, sec_M, ter_M, animal, rarity, *args, **kwargs)



class Mountain(Biome):


	def __init__(self, *args, **kwargs):
		
		self.type = "Mountain"
		self.preposition = "onto a"
		self.pri_R = Item.Stone
		self.sec_R = Item.Wood
		self.ter_R = Item.Wood
		self.pri_M = Mob.Hunter
		self.sec_M = Mob.Hunter
		self.ter_M = Mob.Hunter
		self.animal = Animal.Sheep
		self.rarity = "Common"

		Biome.__init__(type, preposition, pri_R, sec_R, ter_R, pri_M, sec_M, ter_M, animal, rarity, *args, **kwargs)



class Canyon(Biome):


	def __init__(self, *args, **kwargs):
		
		self.type = "Canyon"
		self.preposition = "into a"
		self.pri_R = Item.Stone
		self.sec_R = Item.Wood
		self.ter_R = Item.Quartz
		self.pri_M = Mob.Hunter
		self.sec_M = Mob.Hunter
		self.ter_M = Mob.Assassin
		self.animal = Animal.Sheep
		self.rarity = "Uncommon"

		Biome.__init__(type, preposition, pri_R, sec_R, ter_R, pri_M, sec_M, ter_M, animal, rarity, *args, **kwargs)



class Cave(Biome):


	def __init__(self, *args, **kwargs):
		
		self.type = "Cave"
		self.preposition = "into a"
		self.pri_R = Item.Stone
		self.sec_R = Item.Explosive
		self.ter_R = Item.Quartz
		self.pri_M = Mob.Hunter
		self.sec_M = Mob.Assassin
		self.ter_M = Mob.Hunter
		self.animal = Animal.Sheep
		self.rarity = "Rare"

		Biome.__init__(type, preposition, pri_R, sec_R, ter_R, pri_M, sec_M, ter_M, animal, rarity, *args, **kwargs)



class Monument(Biome):


	def __init__(self, *args, **kwargs):
		
		self.type = "Monument"
		self.preposition = "into a"
		self.pri_R = Item.Stone
		self.sec_R = Item.Quartz
		self.ter_R = Item.Iron
		self.pri_M = Mob.Hunter
		self.sec_M = Mob.Assassin
		self.ter_M = Mob.Ghost
		self.animal = Animal.Chicken
		self.rarity = "Legendary"

		Biome.__init__(type, preposition, pri_R, sec_R, ter_R, pri_M, sec_M, ter_M, animal, rarity, *args, **kwargs)
