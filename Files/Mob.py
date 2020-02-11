"""
Mob.py
NewScript
"""

from Database import MOB_BATCH_SIZE, MOB_TIER_WEIGHTS, NUMBER_OF_MOBS
from random import randrange, choices


class Mob:
	def __init__(self, name, health, weapon, group_count, location, tier):
		self.name = name
		self.health = health
		self.weapon = weapon
		self.group_count = group_count
		self.location = location
		self.tier = tier
		if tier == 1: self.rarity = "Common"
		elif tier == 2: self.rarity = "Uncommon"
		elif tier == 3: self.rarity = "Rare"
	
	def replace_mobs(mob_map, biome_map):
		for loc in range(MOB_BATCH_SIZE):
			while True:
				replace_loc = (randrange(0, 50), randrange(0, 50))
				if mob_map[replace_loc[0]][replace_loc[1]] != None:
					break
			CurrentBiome = biome_map[replace_loc[0]][replace_loc[1]]
			new_mob = choices([CurrentBiome.pri_M, CurrentBiome.sec_M, CurrentBiome.ter_M], weights=MOB_TIER_WEIGHTS, k = 1)
			mob_map[replace_loc[0]][replace_loc[1]] = new_mob
		return mob_map
	
	def spawn_initial_mobs(mob_map, biome_map):
		spawn_locs = [(randrange(0, 50), randrange(0, 50)) for loc in range (NUMBER_OF_MOBS)]
		for loc in spawn_locs:
			CurrentBiome = biome_map[loc[0]][loc[1]]
			new_mob = choices([CurrentBiome.pri_M, CurrentBiome.sec_M, CurrentBiome.ter_M], weights=MOB_TIER_WEIGHTS, k = 1)
			mob_map[loc[0]][loc[1]] = new_mob
		return mob_map	
			
