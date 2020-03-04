"""
Harcrabat Version 0.9
A text-based game of collecting, crafting, and killing
Made by Cameron White & Dallin Guisti
Optimized for python 3.6 & 3.7
"""

from Database import *
from Animal import Animal
from Biome import Biome
from Character import Character
from Environment import Environment
from Item import Item
from Mob import Mob
from Resource import Resource
from Weapon import Weapon
from Projectile import Projectile
from random import choices
from colorama import Fore, Back, init, Style
from time import time, sleep
import msvcrt


### START CODE ###


class Game:

	
	def __init__(self):
	
		## Resources:
		self.Soil = Resource("Soil Pile", "Common")
		self.Wood = Resource("Wood Block", "Common")
		self.Vine = Resource("Vine", "Common")
		self.Fruit = Resource("Fruit", "Common")
		self.Rock = Resource("Rock", "Common")
		self.Water = Resource("Water Supply", "Common")
		self.Sand = Resource("Sand Pile", "Common")
		self.Cacti = Resource("Cacti Block", "Common")
		self.Iron = Resource("Iron Nugget", "Uncommon")
		self.Bone = Resource("Bone", "Common")
		self.Diamond = Resource("Diamond", "Uncommon")
		self.Stone = Resource("Stone", "Common")
		self.Gold = Resource("Gold Nugget", "Uncommon")
		self.Emerald = Resource("Emerald", "Uncommon")
		self.Quartz = Resource("Quartz Shard", "Uncommon")
		self.Explosive = Resource("Explosive", "Common")

		## Items:
		self.HarvesterArmor = Item("Harvester's Armor", None, "Rare")
		self.Protector = Item("Protector", None, "Legendary")
		self.Strawman = Item("Strawman", None, "Rare")
		self.Coffin = Item("Coffin", None, "Legendary")
		self.Ladder = Item("Ladder", None, "Rare")
		self.MobRepellent = Item("Mob Repellent", None, "Legendary")Soil
		self.BottledWave = Item("Bottled Wave", None, "Rare")
		self.BottledWind = Item("Bottled Wind", None, "Legendary")
		self.Glider = Item("Glider", None, "Rare")
		self.Binoculars = Item("Binoculars", None, "Legendary")
		
		## Projectiles:
	
		self.WoodenBall =  Projectile ("Wooden Ball", {self.Wood: 5}, ["Arm"], 13, "Common")
		self.StoneBall = Projectile ("Stone Ball", {self.Wood: 5, self.Stone: 2}, ["Arm"], 15, "Common")
		self.IronBall = Projectile ("Iron Ball", {self.Wood: 5, self.Iron: 2}, ["Arm"], 17, "Common")
		self.DiamondBall = Projectile ("Diamond Ball", {self.Wood: 5, self.Diamond : 2}, ["Arm"], 25, "Uncommon")
		self.WoodenArrow = Projectile("Wooden Arrow", {self.Wood: 3}, ["Bow", "CrossBow"], 17, "Common")
		self.StoneArrow = Projectile("Stone Arrow", {self.Stone: 2, "Wood": 3}, ["Bow", "CrossBow"], 20, "Common")
		self.IronArrow = Projectile("Iron Arrow", {self.Iron: 1, "Wood": 3}, ["Bow", "CrossBow"], 23, "Common")
		self.DiamondArrow = Projectile("Diamond Arrow", {self.Diamond: 1, self.Wood: 3}, ["Bow", "CrossBow"], 26, "Uncommon")
		self.SoilClump = Projectile("Soil Clump", {self.Soil: 4}, ["CombatBucket"], 38, "Common")
		self.SandClump = Projectile("Sand Clump", {self.Sand: 4}, ["CombatBucket"], 38, "Common")
		self.CactusClump = Projectile("Cactus Clump", {self.Cacti: 2}, ["CombatBucket"], 55, "Common")
		self.WoodSpike = Projectile("Wood Spike", {self.Wood: 2}, ["Slingshot"], 17, "Common")
		self.StoneSpike = Projectile("Stone Spike", {self.Stone: 3}, ["Slingshot"], 19, "Common")
		self.IronSpike = Projectile("Iron Spike", {self.Iron: 1, self.Wood: 1}, ["Slingshot"], 21, "Common")
		self.DiamondSpike = Projectile("Diamond Spike", {self.Diamond: 1, self.Wood: 1}, ["Slingshot"], 26, "Uncommon")
		self.CannonBall = Projectile("Cannon Ball", {self.Wood: 10, self.Stone: 15}, ["Cannon"], 125, "Common")
		self.Rocket = Projectile("Rocket", {self.Iron: 15, self.Explosive: 5}, ["RocketLauncher"], 150, "Rare")
		self.Missile = Projectile("Missile", {self.Iron: 15, self.Explosive: 10}, ["MissileLauncher"], 200, "Rare")
		
		## Weapons:
		self.Arm = Weapon("Arm", None, "Range", 1, 90, None, 2, False, "Common")
		self.Bow = Weapon("Bow", {self.Wood: 8, self.Vine: 1}, "Range", 1.25, 60, None, 3, False, "Common")
		self.Crossbow = Weapon("Crossbow", {self.Wood: 10, self.Vine: 2}, "Range", 1.25, 60, None, 3, True, "Common")
		self.CombatBucket = Weapon ("Combat Bucket", {self.Iron: 12}, "Range", 1.75, 100, None, 0, False, "Uncommon")
		self.Slingshot = Weapon("Slingshot", {self.Wood:8, self.Vine:1}, "Range", 0.75, 90, None, 1, False, "Common")
		self.Cannon = Weapon("Cannon", {self.Iron: 1, self.Wood: 200, self.Explosive: 2}, "Range", 10, 100, None, 1, False, "Uncommon")
		self.RocketLauncher = Weapon("Rocket Launcher", {self.Iron: 20, self.Stone: 185, self.Wood: 15, self.Explosive: 6}, "Range", 25, 100, None, 6, True, "Rare")
		self.MissileLauncher = Weapon("Missile Launcher", {self.Iron: 50, self.Stone: 200, self.Wood: 50, self.Explosive: 8}, "Range", 40, 100, None, 8, True, "Legendary")
		self.Fists = Weapon("Fists", None, "Melee", 0.5, 100, 5, 0, None, "Common")
		self.BoneBlade = Weapon("Bone Blade", {self.Bone: 3}, "Melee", 1.25, 90, 10, 0, None, "Common")
		self.BoneStriker = Weapon("Bone Striker", {self.Bone: 8}, "Melee", 1.25, 90, 25, 0, None, "Uncommon")
		self.WoodenSword = Weapon("Wooden Sword", {self.Wood: 8}, "Melee", 1, 80, 17, 0, None, "Common")
		self.StoneSword = Weapon("Stone Sword", {self.Stone: 10, self.Wood: 3},"Melee", 1, 80, 20, 0, None, "Common")
		self.IronSword = Weapon("Iron Sword", {self.Iron: 10, self.Wood: 3}, "Melee", 1, 80, 23, 0, None, "Uncommon")
		self.DiamondSword = Weapon("Diamond Sword", {self.Diamond: 10, self.Wood: 3}, "Melee", 1, 80, 26, 0, None, "Rare")
		self.WoodenAxe = Weapon("Wooden Axe", {self.Wood: 9}, "Melee", 1.5, 70, 26, 0, None, "Common")
		self.StoneAxe = Weapon("Stone Axe", {self.Stone: 10, self.Wood: 4}, "Melee", 1.5, 70, 30, 0, None, "Common")
		self.IronAxe = Weapon("Iron Axe", {self.Iron: 10, self.Wood: 4}, "Melee", 1.5, 70, 34, 0, None, "Uncommon")
		self.DiamondAxe = Weapon("Diamond Axe", {self.Diamond: 10, self.Wood: 4}, "Melee", 1.5, 70, 38, 0, None, "Rare")
		self.WoodenSpear = Weapon("Wooden Spear", {self.Wood: 10}, "Melee", 1.75, 60, 30, 1, None, "Common")
		self.StoneSpear = Weapon("Stone Spear", {self.Stone: 10, self.Wood: 5}, "Melee", 1.75, 60, 35, 1, None, "Common")
		self.IronSpear = Weapon("Iron Spear", {self.Iron: 10, self.Wood: 5}, "Melee", 1.75, 60, 40, 1, None, "Uncommon")
		self.DiamondSpear = Weapon("Diamond Spear", {self.Diamond: 10, self.Wood: 5}, "Melee", 1.75, 60, 45, 1, None, "Rare")
		self.WoodenBoomerang = Weapon("Wooden Boomerang", {self.Wood: 12}, "Melee", 3, 90, 40, 2, None, "Common")
		self.StoneBoomerang = Weapon("Stone Boomerang", {self.Stone: 10, self.Wood: 6}, "Melee", 3, 90, 50, 2, None, "Common")
		self.IronBoomerang = Weapon("Iron Boomerang", {self.Iron: 10, self.Wood: 6}, "Melee", 3, 90, 60, 2, None, "Uncommon")
		self.DiamondBoomerang = Weapon("Diamond Boomerang", {self.Diamond: 10, self.Wood: 6}, "Melee", 3, 90, 70, 2, None, "Rare")
		self.Bomb = Weapon("Bomb", {self.Stone: 25, self.Wood: 25, self.Explosive: 5}, "Melee", 15, 100, 100, 0, None, "Common")
		self.Grenade = Weapon("Grenade", {self.Stone: 4, self.Wood: 4, self.Explosive: 2}, "Melee", 8, 100, 75, 0, None, "Common")
		self.Dynamite = Weapon("Dynamite", {self.Explosive: 1}, "Melee", 1, 100, 50, None, False, "Common")

		## Mobs:
		self.Fighter = Mob("Fighter", 75, self.WoodenSword, 1, None, 3)
		self.Predator = Mob("Predator", 100, self.IronSword, 1, None, 2)
		self.Goblin = Mob("Goblin", 200, self.DiamondSword, 1, None, 1)
		self.Destroyer = Mob("Destroyer", 50, self.WoodenAxe, 1, None, 3)
		self.Annihilator = Mob("Annihilator", 50, self.IronSpear, 1, None, 2)
		self.Troll = Mob("Troll", 200, self.Slingshot, 1, None, 1) #### Slingshot
		self.Raider = Mob("Raider", 25, self.Fists, 3, None, 3)
		self.Minion = Mob("Minion", 20, self.Fists, 5, None, 2)
		self.Zombie = Mob("Zombie", 200, self.Arm, 3, None, 1)
		self.Defender = Mob("Defender", 100, self.BoneBlade, 1, None, 3)
		self.Guardian = Mob("Guardian", 150, self.BoneBlade, 1, None, 2)
		self.Skeleton = Mob("Skeleton", 200, self.BoneStriker, 1, None, 1)
		self.Hunter = Mob("Hunter", 75, self.Bow, 1, None, 3) #### Bow
		self.Assasin = Mob("Assassin", 100, self.Crossbow, 1, None, 2) #### Crossbow
		self.Ghoul = Mob("Ghoul", 200, self.DiamondBoomerang, 1, None, 1)

		## Animals:
		self.Chicken = Animal()
		self.Rabbit = Animal()
		self.Cow = Animal()
		self.Fish = Animal()
		self.Sheep = Animal()

		## Biomes:
		self.Forest = Biome("Forest", "into a", self.Wood, self.Soil, self.Soil, self.Fighter, self.Fighter, self.Fighter, self.Chicken, None, None, "Common")
		self.Jungle = Biome("Jungle", "into a", self.Wood, self.Soil, self.Emerald, self.Fighter, self.Fighter, self.Predator, self.Chicken, None, None, "Uncommon")
		self.Grove = Biome("Grove", "into a", self.Wood, self.Fruit, self.Emerald, self.Fighter, self.Predator, self.Fighter, self.Chicken, None, None, "Rare")
		self.Garden = Biome("Garden", "into a", self.Wood, self.Emerald, self.Gold, self.Fighter, self.Predator, self.Goblin, self.Chicken, self.HarvesterArmor, self.Protector, "Legendary")
		self.Desert = Biome("Desert", "into a", self.Sand, self.Stone, self.Stone, self.Destroyer, self.Destroyer, self.Destroyer, self.Rabbit, None, None, "Common")
		self.Tundra = Biome("Tundra", "into a", self.Sand, self.Stone, self.Iron, self.Destroyer, self.Destroyer, self.Annihilator, self.Rabbit, None, None, "Uncommon")
		self.Badland = Biome("Badland", "into a", self.Sand, self.Cacti, self.Iron, self.Destroyer, self.Annihilator, self.Destroyer, self.Rabbit, None, None, "Rare")
		self.Temple = Biome("Temple", "into a", self.Sand, self.Iron, self.Diamond, self.Destroyer, self.Annihilator, self.Troll, self.Rabbit, self.Strawman, self.Coffin, "Legendary")
		self.Prairie = Biome("Prairie", "into a", self.Soil, self.Water, self.Water, self.Raider, self.Raider, self.Raider, self.Cow, None, None, "Common")
		self.Meadow = Biome("Meadow", "into a", self.Soil, self.Water, self.Diamond, self.Raider, self.Raider, self.Minion, self.Cow, None, None, "Uncommon")
		self.Swamp = Biome("Swamp", "into a", self.Soil, self.Vine, self.Diamond, self.Raider, self.Minion, self.Raider, self.Cow, None, None, "Rare")
		self.Fort = Biome("Fort", "into a", self.Soil, self.Diamond, self.Quartz, self.Raider, self.Minion, self.Zombie, self.Cow, self.Ladder, self.MobRepellent, "Legendary")
		self.Lake = Biome("Lake", "into a", self.Water, self.Sand, self.Sand, self.Defender, self.Defender, self.Defender, self.Fish, None, None, "Common")
		self.Beach = Biome("Beach", "into a", self.Water, self.Sand, self.Gold, self.Defender, self.Defender, self.Guardian, self.Fish, None, None, "Uncommon")
		self.Island = Biome("Island", "onto an", self.Water, self.Bone, self.Gold, self.Defender, self.Guardian, self.Defender, self.Fish, None, None, "Rare")
		self.Shipwreck =Biome("Shipwreck", "into a", self.Water, self.Gold, self.Emerald, self.Defender, self.Guardian, self.Skeleton, self.Fish, self.BottledWave, self.BottledWind, "Legendary")
		self.Mountain = Biome("Mountain", "onto a", self.Stone, self.Wood, self.Wood, self.Hunter, self.Hunter, self.Hunter, self.Sheep, None, None, "Common")
		self.Canyon = Biome("Canyon", "into a", self.Stone, self.Wood, self.Quartz, self.Hunter, self.Hunter, self.Assasin, self.Sheep, None, None, "Uncommon")
		self.Cave = Biome("Cave", "into a", self.Stone, self.Explosive, self.Quartz, self.Hunter, self.Assasin, self.Hunter, self.Sheep, None, None, "Rare")
		self.Monument = Biome("Monument", "into a", self.Stone, self.Quartz, self.Iron, self.Hunter, self.Assasin, self.Ghoul, self.Sheep, self.Glider, self.Binoculars, "Legendary")

		## Environments:
		self.Woodlands = Environment(self.Forest, self.Jungle, self.Grove, self.Garden)
		self.Plains = Environment(self.Desert, self.Tundra, self.Badland, self.Temple)
		self.Grasslands = Environment(self.Prairie, self.Meadow, self.Swamp, self.Fort)
		self.Waterlands = Environment(self.Lake, self.Beach, self.Island, self.Shipwreck)
		self.Rockylands = Environment(self.Mountain, self.Canyon, self.Cave, self.Monument)
		
		## Player:	
		self.Player = Character("Player 1", 0, [], [], [[time() - COLLECT_DELAY for square in range(51)] for row in range(51)], 100, 100, {}, None, None, [26,26], "North", time())
		
		## Misc:
		self.items = []
		for item in ITEMS:
			item_obj = eval("self." + item)
			self.items.append(item_obj)
		
		self.last_spawn_time = time()
		
		self.mob_map = [[None for square in range(51)] for row in range(51)]
		self.initial_mobs_spawned = False
		
		## Startup:
		self.startup()


	### GAME FUNCTIONS ###
	

	def create_player(self):
		desired_name = input("Enter your name:\n| ")
		eval(PRINT_SEPARATER)
		self.Player.set_name(desired_name)
		self.Player.inventory = {item: 0 for item in self.items}
		
	def choose_biome(self, env):
		EnvClass = eval("self." + env)
		BiomeChoice = choices([EnvClass.pri_B, EnvClass.sec_B, EnvClass.ter_B, EnvClass.structure], weights=BIOME_WEIGHTS)[0]
		return BiomeChoice

	
	def load_game_map(self):
		print("Loading map")

		## Preload game_map:
		print("\tCreating Seed")
		game_map = [[None 
				if col_index in [0,52]
				or row_index in [0,52]
				else choices(("Woodlands", "Plains", "Grasslands", "Waterlands", "Rockylands"))[0]
			for col_index in range(53)]
			for row_index in range(53)]
		
		## Choose Environments:
		print("\tGenerating Chunks")
		for rep in range(ENV_CLEANUP_FACTOR):
			game_map = [[None
					if col_index in [0,52]
					or row_index in [0,52]
					else Environment.choose([game_map[row_index-1][col_index-1], game_map[row_index-1][col_index], game_map[row_index-1][col_index+1], game_map[row_index][col_index-1], game_map[row_index][col_index+1], game_map[row_index+1][col_index-1], game_map[row_index+1][col_index], game_map[row_index+1][col_index+1]])
				for col_index in range(len(game_map[row_index]))]
				for row_index in range(len(game_map))]
		game_map = [[Env for Env in row[1:-1]] for row in game_map[1:-1]]

		## Choose Biomes:
		print("\tGenerating Terrain")
		biome_map = [[self.choose_biome(Env)
			for Env in row]
			for row in game_map]
		
		self.Player.game_map = game_map
		self.Player.biome_map = biome_map

		return game_map, biome_map


	def run_game(self):
		## Wait for keypress:
		while True:
			while not msvcrt.kbhit():
				self.update_game()
				#### Update game
			key_input = msvcrt.getch()
			
			## Respond to keypress:
			if key_input in KEY_BINDINGS:
				eval(KEY_BINDINGS[key_input][0])


	def update_game(self):
		if not self.initial_mobs_spawned:
			self.mob_map = Mob.spawn_initial_mobs(self.mob_map, self.Player.biome_map)
			self.initial_mobs_spawned = True
			self.last_spawn_time = time()
		####elif time() - self.last_spawn_time >= MOB_REPLACE_DELAY:
		####	self.mob_map = Mob.replace_mobs(self.mob_map, self.Player.biome_map)
		####	self.last_spawn_time = time()
		new_mob_map = Mob.move_mobs(Mob, self.mob_map, self.Player.location)
		if new_mob_map: self.mob_map = new_mob_map
		for i, row in enumerate(self.mob_map):
			for j, loc in enumerate(row):
				if [i,j] == self.Player.location: print ("PP", end="")
				elif loc != None:
					if loc.hostile == True: sdf = "H"
					else:
						sdf = "N"
					print (str(loc.weapon.range)+sdf, end="")
				else: print ("--", end="")
			print("")
		print (self.mob_map[self.Player.location[0]][self.Player.location[1]])
		sleep (5)
		#### Update health and energy
		#### Regenerate resources in exhausted squares
		#### Spawn Animals


	### COMMAND FUNCTIONS ###


	def help(self):
		[print(command + ": " + COMMANDS[command]) for command in COMMANDS]


	def start(self):
		self.create_player()
		game_map, biome_map = self.load_game_map()
		eval(PRINT_SEPARATER)
		self.Player.describe_spawnpoint()
		self.run_game()
		
	
	def exit(self):
		quit ()


	def controls(self):
		for key in KEY_BINDINGS:
			if key == b" ": letter = "SPACE"
			else: letter = key.decode("utf-8")
			print(letter + ": " + KEY_BINDINGS[key][1])		


	### MANAGER FUNCTIONS ###


	def command_input(self):
		eval(PRINT_SEPARATER)
		command = (input("| ")).lower()
		eval(PRINT_SEPARATER)
		if command in COMMANDS: eval("self." + command + "()")
		else: print("Invalid Command")

		
	def startup(self):
		init()
		print("Harcrabat version 0.8")
		print("Type 'help' for the command list.")
		while True:
			self.command_input()
		
	
if __name__ == "__main__": NewScript = Game()
