"""
Mob.py
NewScript
"""

from Database import MOB_BATCH_SIZE, MOB_TIER_WEIGHTS, NUMBER_OF_MOBS, MOB_MOVE_BATCH_SIZE
from random import randrange, choices


class Mob:
	def __init__(self, name, health, weapon, group_count, location, tier):
		self.name = name
		self.health = health
		self.weapon = weapon
		self.group_count = group_count
		self.location = location
		self.tier = tier
		if tier == 1:
			self.rarity = "Common"
		elif tier == 2:
			self.rarity = "Uncommon"
		elif tier == 3:
			self.rarity = "Rare"
	
	def replace_mobs(mob_map, biome_map):
		for loc in range(MOB_BATCH_SIZE):
			while True:
				replace_loc = (randrange(0, 50), randrange(0, 50))
				if mob_map[replace_loc[0]][replace_loc[1]] != None:
					break
			CurrentBiome = biome_map[replace_loc[0]][replace_loc[1]]
			new_mob = choices([CurrentBiome.pri_M, CurrentBiome.sec_M, CurrentBiome.ter_M], weights=MOB_TIER_WEIGHTS, k = 1)[0]
			mob_map[replace_loc[0]][replace_loc[1]] = new_mob
		return mob_map
	
	def spawn_initial_mobs(mob_map, biome_map):
		spawn_locs = [(randrange(0, 50), randrange(0, 50)) for loc in range (NUMBER_OF_MOBS)]
		for loc in spawn_locs:
			CurrentBiome = biome_map[loc[0]][loc[1]]
			new_mob = choices([CurrentBiome.pri_M, CurrentBiome.sec_M, CurrentBiome.ter_M], weights=MOB_TIER_WEIGHTS, k = 1)[0]
			mob_map[loc[0]][loc[1]] = new_mob
		return mob_map
				
	def move(moving_mob, loc, mob_map, move_direction):
		if move_direction == "North": new_mob_loc = (loc[0]-1, loc[1])
		elif move_direction == "South": new_mob_loc = (loc[0]+1, loc[1])
		elif move_direction == "West": new_mob_loc = (loc[0], loc[1]-1)
		elif move_direction == "East": new_mob_loc = (loc[0], loc[1]+1)
		try:
			if mob_map[new_mob_loc[0]][new_mob_loc[1]] == None:
				mob_map[new_mob_loc[0]][new_mob_loc[1]] = moving_mob
				mob_map[loc[0]][loc[1]] = None
		except: pass
		return mob_map
	
	def move_mobs(self, mob_map, player_location):
		mob_occupied_locs = [[(row, col) for col in range(51) if mob_map[row][col]] for row in range(51)]
		mob_occupied_locs = [i for j in mob_occupied_locs for i in j]
		moving_mob_locs = choices(mob_occupied_locs, weights = None, k = MOB_MOVE_BATCH_SIZE)
		for loc in moving_mob_locs:
			moving_mob = mob_map[loc[0]][loc[1]]
			currently_hostile = self.be_hostile(self, moving_mob, loc, player_location, mob_map)
			if not currently_hostile:
				move_direction = choices(["North", "West", "East", "South"], weights = None, k=1)[0]
				self.move(moving_mob, loc, mob_map, move_direction)
				
	def be_hostile(self, TheMob, loc, player_location, mob_map):
		try:
			if mob_map[loc[0]-1][loc[1]] == player_location:
				rel_pos = "North"
		except: pass
		try:
			if mob_map[loc[0]][loc[1]-1] == player_location:
				rel_pos = "West"
		except: pass
		try:
			if mob_map[loc[0]][loc[1]+1] == player_location:
				rel_pos = "East"
		except: pass
		try:
			if mob_map[loc[0]+1][loc[1]] == player_location:
				rel_pos = "South"
		except: pass
		try: rel_pos
		except: return False
		if TheMob.weapon.range == 0:
			if rel_pos == "North":
				self.move(TheMob, mob_map, "South")
			if rel_pos == "West":
				self.move(TheMob, mob_map, "East")
			if rel_pos == "East":
				self.move(TheMob, mob_map, "West")
			if rel_pos == "South":
				self.move(TheMob, mob_map, "North")
		else:
			for movement in range(TheMob.weapon.range):
				self.move(TheMob, loc, mob_map, rel_pos)
		
			