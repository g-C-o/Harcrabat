"""
Mob.py
Harcrabat
"""

from Database import MOB_BATCH_SIZE, MOB_TIER_WEIGHTS, NUMBER_OF_MOBS, MOB_MOVE_BATCH_SIZE
from random import randrange, sample, choices
import Item



class Mob:


	def __init__(self, name, health, weapon, group_count, location, level):
		self.name = name
		self.health = health
		self.weapon = weapon
		self.group_count = group_count
		self.location = location
		self.hostile = False

		if level == 1:
			self.rarity = "Common"
		elif level == 2:
			self.rarity = "Uncommon"
		elif level == 3:
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
		print ("spawn initial mobs")
		spawn_locs = [(randrange(0, 50), randrange(0, 50)) for loc in range (NUMBER_OF_MOBS)]
		for loc in spawn_locs:
			CurrentBiome = biome_map[loc[0]][loc[1]]
			new_mob_type = choices([CurrentBiome.pri_M, CurrentBiome.sec_M, CurrentBiome.ter_M], weights=MOB_TIER_WEIGHTS, k = 1)[0]
			#### Below: Fix method after data restructuring (v0.9)
			new_mob = Mob(new_mob_type.name, new_mob_type.health, new_mob_type.weapon, new_mob_type.group_count, new_mob_type.location, new_mob_type.tier)
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
	
	
	def be_hostile(self, mob_map, player_location, loc):
		print (self.weapon.range)
		try:
			if [loc[0]-1,loc[1]] == player_location:
				rel_pos = "South"
		except IndexError: pass
		try:
			if [loc[0],loc[1]-1] == player_location:
				rel_pos = "East"
		except IndexError: pass
		try:
			if [loc[0],loc[1]+1] == player_location:
				rel_pos = "West"
		except IndexError: pass
		try:
			if [loc[0]+1,loc[1]] == player_location:
				rel_pos = "North"
		except: pass
		if self.weapon.range == 0:
			if rel_pos == "North":
				mob_map = self.move(loc, mob_map, "South")
			if rel_pos == "West":
				mob_map = self.move(loc, mob_map, "East")
			if rel_pos == "East":
				mob_map = self.move(loc, mob_map, "West")
			if rel_pos == "South":
				mob_map = self.move(loc, mob_map, "North")
		else:
			for movement in range(self.weapon.range):
				mob_map = self.move(loc, mob_map, rel_pos)
		return mob_map
	
	
	def move_mobs(self, mob_map, player_location):
		#### In version 0.9 (data restructuring), fix:
		#### Mobs in hostile vicinity wait one turn before hostility sequence
		#### Mobs stay hostile when in same square as player, but do not see player around them
		#### Mobs cannot share squares:
		#### - More than one 0-range hostile mob cannot go into the player's square
		mob_occupied_squares = [[(row, col) for col in range(51) if mob_map[row][col] != None] for row in range(51)]
		mob_occupied_locs = []
		for row in mob_occupied_squares: 
			if row == []: continue
			for square in row:
				mob_occupied_locs.append(square)
		moving_mob_locs = sample(mob_occupied_locs, k = MOB_MOVE_BATCH_SIZE)
		for loc in mob_occupied_locs:
			####try:
			####	print (mob_map[looc[0]][looc[1]].hostile)
			####except: pass
			moving_mob = mob_map[loc[0]][loc[1]]
			if moving_mob.hostile == True:
				mob_map = moving_mob.be_hostile(mob_map, player_location, loc)
			else:
				currently_hostile = self.check_hostility(moving_mob, loc, player_location, mob_map)
				if currently_hostile:
					print (loc, "\n")
					for locd in mob_occupied_locs:
						try:
							print (mob_map[locd[0]][locd[1]].hostile, end="")
						except: pass
					mob_map[loc[0]][loc[1]].hostile = True
					print ("")
					looc = loc
					for locd in mob_occupied_locs:
						try:
							if mob_map[locd[0]][locd[1]].hostile:
								print (mob_map[locd[0]][locd[1]])
						except: pass
				if not currently_hostile:
					if loc in moving_mob_locs:
						move_direction = choices(["North", "West", "East", "South"], weights = None, k=1)[0]
						mob_map = self.move(moving_mob, loc, mob_map, move_direction)
		return mob_map

				
	def check_hostility(TheMob, loc, player_location, mob_map):
		try:
			if [loc[0]-1,loc[1]] == player_location:
				rel_pos = "South"
		except IndexError: pass
		try:
			if [loc[0],loc[1]-1] == player_location:
				rel_pos = "East"
		except IndexError: pass
		try:
			if [loc[0],loc[1]+1] == player_location:
				rel_pos = "West"
		except IndexError: pass
		try:
			if [loc[0]+1,loc[1]] == player_location:
				rel_pos = "North"
		except: pass
		try:
			rel_pos
			return True
		except UnboundLocalError: return False



class Level1Mob(Mob):


	def __init__(self, name, health, weapon, group_count, location, *args, **kwargs):

		self.level = 1

		Mob.__init__(level, *args, **kwargs)



class Level2Mob(Mob):


	def __init__(self, name, health, weapon, group_count, location, *args, **kwargs):

		self.level = 2

		Mob.__init__(level, *args, **kwargs)



class Level3Mob(Mob):


	def __init__(self, name, health, weapon, group_count, location, *args, **kwargs):

		self.level = 3
		self.health = 200

		Mob.__init__(level, health, *args, **kwargs)



### LEVEL 1 MOBS ###



class Fighter(Level1Mob):
	
	
	def __init__(self, name, location, *args, **kwargs):
		
		self.type = "Fighter"
		self.health = 75
		self.weapon = Item.WoodChunkenSword()
		self.group_count = 1
		
		Level1Mob.__init__(type, health, weapon, group_count, *args, **kwargs)
	
	

class Destroyer(Level1Mob):
	
	
	def __init__(self, name, location, *args, **kwargs):
		
		self.type = "Destroyer"
		self.health = 50
		self.weapon = Item.WoodChunkenAxe()
		self.group_count = 1
		
		Level1Mob.__init__(type, health, weapon, group_count, *args, **kwargs)



class Raider(Level1Mob):
	
	
	def __init__(self, name, location, *args, **kwargs):
		
		self.type = "Raider"
		self.health = 25
		self.weapon = Item.Fists()
		self.group_count = 3
		
		Level1Mob.__init__(type, health, weapon, group_count, *args, **kwargs)



class Defender(Level1Mob):
	
	
	def __init__(self, name, location, *args, **kwargs):
		
		self.type = "Defender"
		self.health = 100
		self.weapon = Item.BoneBlade()
		self.group_count = 1
		
		Level1Mob.__init__(type, health, weapon, group_count, *args, **kwargs)



class Hunter(Level1Mob):
	
	
	def __init__(self, name, location, *args, **kwargs):
		
		self.type = "Hunter"
		self.health = 75
		self.weapon = Item.Bow()
		self.group_count = 1
		
		Level1Mob.__init__(type, health, weapon, group_count, *args, **kwargs)



### LEVEL 2 MOBS ###



class Predator(Level2Mob):
	
	
	def __init__(self, name, location, *args, **kwargs):
		
		self.type = "Predator"
		self.health = 100
		self.weapon = Item.IronSword()
		self.group_count = 1
		
		Level2Mob.__init__(type, health, weapon, group_count, *args, **kwargs)



class Annihilator(Level2Mob):
	
	
	def __init__(self, name, location, *args, **kwargs):
		
		self.type = "Annihilator"
		self.health = 50
		self.weapon = Item.IronSpear()
		self.group_count = 1
		
		Level2Mob.__init__(type, health, weapon, group_count, *args, **kwargs)



class Minion(Level2Mob):
	
	
	def __init__(self, name, location, *args, **kwargs):
		
		self.type = "Minion"
		self.health = 20
		self.weapon = Item.Fists()
		self.group_count = 5
		
		Level2Mob.__init__(type, health, weapon, group_count, *args, **kwargs)



class Guardian(Level2Mob):
	
	
	def __init__(self, name, location, *args, **kwargs):
		
		self.type = "Guardian"
		self.health = 150
		self.weapon = Item.BoneBlade()
		self.group_count = 1
		
		Level2Mob.__init__(type, health, weapon, group_count, *args, **kwargs)



class Assassin(Level2Mob):
	
	
	def __init__(self, name, location, *args, **kwargs):
		
		self.type = "Assassin"
		self.health = 100
		self.weapon = Item.Crossbow()
		self.group_count = 1
		
		Level2Mob.__init__(type, health, weapon, group_count, *args, **kwargs)



### LEVEL 3 MOBS ###



class Goblin(Level3Mob):
	
	
	def __init__(self, name, location, *args, **kwargs):
		
		self.type = "Goblin"
		self.weapon = Item.DiamondSword()
		self.group_count = 1
		
		Level3Mob.__init__(type, weapon, group_count, *args, **kwargs)



class Troll(Level3Mob):
	
	
	def __init__(self, name, location, *args, **kwargs):
		
		self.type = "Troll"
		self.weapon = Item.Slingshot()
		self.group_count = 1
		
		Level3Mob.__init__(type, weapon, group_count, *args, **kwargs)



class Zombie(Level3Mob):
	
	
	def __init__(self, name, location, *args, **kwargs):
		
		self.type = "Zombie"
		self.weapon = Item.Arm()
		self.group_count = 3
		
		Level3Mob.__init__(type, weapon, group_count, *args, **kwargs)



class Skeleton(Level3Mob):
	
	
	def __init__(self, name, location, *args, **kwargs):
		
		self.type = "Skeleton"
		self.weapon = Item.BoneStriker()
		self.group_count = 1
		
		Level3Mob.__init__(type, weapon, group_count, *args, **kwargs)



class Ghost(Level3Mob):
	
	
	def __init__(self, name, location, *args, **kwargs):
		
		self.type = "Ghost"
		self.weapon = Item.DiamondBoomerang()
		self.group_count = 1
		
		Level3Mob.__init__(type, weapon, group_count, *args, **kwargs)