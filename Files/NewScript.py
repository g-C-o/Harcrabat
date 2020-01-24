"""
NewScript Version 0.6
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
from random import choices
from colorama import Fore, Back, init, Style
from time import time
import msvcrt


### START CODE ###


class Game:

	
	def __init__(self):
		
		## Sub-classes:
		self.Character = Character
		self.Resource = Resource
		self.Item = Item
		self.Mob = Mob
		self.Animal = Animal
		self.Biome = Biome
		self.Environment = Environment
		
		## Player:	
		self.Player = self.Character("Player 1", 0, [], [], [[time() - COLLECT_DELAY for square in range(50)] for row in range(50)], 100, 100, {}, None, None, [26,26], "North", time())

		## Resources:
		self.Soil = self.Resource("Soil Pile", 360, "Soil Piles")
		self.Wood = self.Resource("Wood Block", 252, "Wood Blocks")
		self.Vine = self.Resource("Vine", 16, "Vines")
		self.Fruit = self.Resource("Fruit", 56, "Fruits")
		self.Rock = self.Resource("Rock", 100, "Rocks")
		self.Water = self.Resource("Water Supply", 180, "Water Supplies")
		self.Sand = self.Resource("Sand Pile", 160, "Sand Piles")
		self.Cacti = self.Resource("Cacti Block", 16, "Cacti Blocks")
		self.Iron = self.Resource("Iron Nugget", 124, "Iron Nuggets")
		self.Bone = self.Resource("Bone", 16, "Bones")
		self.Diamond = self.Resource("Diamond", 8, "Diamonds")
		self.Stone = self.Resource("Stone", 216, "Stone Blocks")
		self.Gold = self.Resource("Gold Nugget", 40, "Gold Nuggets")
		self.Emerald = self.Resource("Emerald", 8, "Emeralds")
		self.Quartz = self.Resource("Quartz Shard", 20, "Quartz Shards")
		self.Flint = self.Resource("Flint Shard", None, "Flint Shards")

		## Items:
		self.HarvesterArmor = self.Item("Harvester's Armor", None, "Rare")
		self.Protector = self.Item("Protector", None, "Rare")
		self.Strawman = self.Item("Strawman", None, "Rare")
		self.Coffin = self.Item("Coffin", None, "Rare")
		self.Ladder = self.Item("Ladder", None, "Rare")
		self.MobRepellant = self.Item("Mob Repellant", None, "Rare")
		self.BottledWave = self.Item("Bottled Wave", None, "Rare")
		self.BottledWind = self.Item("Bottled Wind", None, "Rare")
		self.Glider = self.Item("Glider", None, "Rare")
		self.Binoculars = self.Item("Binoculars", None, "Rare")
		self.TestItem = self.Item("Test Item", {"Wood": 3, "Soil": 1}, "Common")

		## Mobs:
		self.Fighter = self.Mob()
		self.Predator = self.Mob()
		self.Goblin = self.Mob()
		self.Destroyer = self.Mob()
		self.Annihilator = self.Mob()
		self.Troll = self.Mob()
		self.Raider = self.Mob()
		self.Minion = self.Mob()
		self.Zombie = self.Mob()
		self.Defender = self.Mob()
		self.Guardian = self.Mob()
		self.Skeleton = self.Mob()
		self.Hunter = self.Mob()
		self.Assasin = self.Mob()
		self.Ghoul = self.Mob()

		## Animals:
		self.Chicken = self.Animal()
		self.Rabbit = self.Animal()
		self.Cow = self.Animal()
		self.Fish = self.Animal()
		self.Sheep = self.Animal()

		## Biomes:
		self.Forest = self.Biome("Forest", "into a", self.Wood, self.Soil, self.Soil, self.Fighter, self.Fighter, self.Fighter, self.Chicken, None, None)
		self.Jungle = self.Biome("Jungle", "into a", self.Wood, self.Soil, self.Emerald, self.Fighter, self.Fighter, self.Predator, self.Chicken, None, None)
		self.Grove = self.Biome("Grove", "into a", self.Wood, self.Fruit, self.Emerald, self.Fighter, self.Predator, self.Fighter, self.Chicken, None, None)
		self.Garden = self.Biome("Garden", "into a", self.Wood, self.Emerald, self.Gold, self.Fighter, self.Predator, self.Goblin, self.Chicken, self.HarvesterArmor, self.Protector)
		self.Desert = self.Biome("Desert", "into a", self.Sand, self.Stone, self.Stone, self.Destroyer, self.Destroyer, self.Destroyer, self.Rabbit, None, None)
		self.Tundra = self.Biome("Tundra", "into a", self.Sand, self.Stone, self.Quartz, self.Destroyer, self.Destroyer, self.Annihilator, self.Rabbit, None, None)
		self.Badland = self.Biome("Badland", "into a", self.Sand, self.Cacti, self.Quartz, self.Destroyer, self.Annihilator, self.Destroyer, self.Rabbit, None, None)
		self.Temple = self.Biome("Temple", "into a", self.Sand, self.Quartz, self.Iron, self.Destroyer, self.Annihilator, self.Troll, self.Rabbit, self.Strawman, self.Coffin)
		self.Prairie = self.Biome("Prairie", "into a", self.Soil, self.Water, self.Water, self.Raider, self.Raider, self.Raider, self.Cow, None, None)
		self.Meadow = self.Biome("Meadow", "into a", self.Soil, self.Water, self.Diamond, self.Raider, self.Raider, self.Minion, self.Cow, None, None)
		self.Swamp = self.Biome("Swamp", "into a", self.Soil, self.Vine, self.Diamond, self.Raider, self.Minion, self.Raider, self.Cow, None, None)
		self.Fort = self.Biome("Fort", "into a", self.Soil, self.Diamond, self.Iron, self.Raider, self.Minion, self.Zombie, self.Cow, self.Ladder, self.MobRepellant)
		self.Lake = self.Biome("Lake", "into a", self.Water, self.Sand, self.Water, self.Defender, self.Defender, self.Defender, self.Fish, None, None)
		self.Beach = self.Biome("Beach", "into a", self.Water, self.Sand, self.Diamond, self.Defender, self.Defender, self.Guardian, self.Fish, None, None)
		self.Island = self.Biome("Island", "onto an", self.Water, self.Bone, self.Diamond, self.Defender, self.Guardian, self.Defender, self.Fish, None, None)
		self.Shipwreck =self.Biome("Shipwreck", "into a", self.Water, self.Gold, self.Quartz, self.Defender, self.Guardian, self.Skeleton, self.Fish, self.BottledWave, self.BottledWind)
		self.Mountain = self.Biome("Mountain", "onto a", self.Stone, self.Wood, self.Sand, self.Hunter, self.Hunter, self.Hunter, self.Sheep, None, None)
		self.Canyon = self.Biome("Canyon", "into a", self.Stone, self.Wood, self.Gold, self.Hunter, self.Hunter, self.Assasin, self.Sheep, None, None)
		self.Cave = self.Biome("Cave", "into a", self.Stone, self.Flint, self.Gold, self.Hunter, self.Assasin, self.Hunter, self.Sheep, None, None)
		self.Monument = self.Biome("Monument", "into a", self.Stone, self.Iron, self.Emerald, self.Hunter, self.Assasin, self.Ghoul, self.Sheep, self.Glider, self.Binoculars)

		## Environments:
		self.Woodlands = self.Environment(self.Forest, self.Jungle, self.Grove, self.Garden)
		self.Plains = self.Environment(self.Desert, self.Tundra, self.Badland, self.Temple)
		self.Grasslands = self.Environment(self.Prairie, self.Meadow, self.Swamp, self.Fort)
		self.Waterlands = self.Environment(self.Lake, self.Beach, self.Island, self.Shipwreck)
		self.Rockylands = self.Environment(self.Mountain, self.Canyon, self.Cave, self.Monument)

		self.startup()


	### GAME FUNCTIONS ###
	

	def create_player(self):
		desired_name = input("Enter your name:\n| ")
		eval(PRINT_SEPARATER)
		self.Player.set_name(desired_name)

	
	def load_map(self):
		print("Loading map")

		## Preload map:
		print("\tCreating Seed")
		map = [[None 
				if col_index in [0,51]
				or row_index in [0,51]
				else choices(("Woodlands", "Plains", "Grasslands", "Waterlands", "Rockylands"))[0]
			for col_index in range(52)]
			for row_index in range(52)]
		
		## Choose Environments:
		print("\tGenerating Chunks")
		for rep in range(ENV_CLEANUP_FACTOR):
			map = [[None
					if col_index in [0,51]
					or row_index in [0,51]
					else Environment.choose([map[row_index-1][col_index-1], map[row_index-1][col_index], map[row_index-1][col_index+1], map[row_index][col_index-1], map[row_index][col_index+1], map[row_index+1][col_index-1], map[row_index+1][col_index], map[row_index+1][col_index+1]])
				for col_index in range(len(map[row_index]))]
				for row_index in range(len(map))]
		map = [[Env for Env in row[1:-1]] for row in map[1:-1]]

		## Choose Biomes:
		print("\tGenerating Terrain")
		biome_map = [[self.Biome.choose(self, Env)
			for Env in row]
			for row in map]
		
		self.Player.map = map
		self.Player.biome_map = biome_map

		return map, biome_map


	def run_game(self):
		## Wait for keypress:
		while True:
			while not msvcrt.kbhit():
				pass
				#### Update game
			key_input = msvcrt.getch()
			
			## Respond to keypress:
			if key_input in KEY_BINDINGS:
				eval(KEY_BINDINGS[key_input][0])


	def update_game(self):
		#### Update health and energy
		#### Regenerate resources in exhausted squares
		#### Spawn stuff
		pass


	### COMMAND FUNCTIONS ###


	def help(self):
		[print(command + ": " + COMMANDS[command]) for command in COMMANDS]


	def start(self):
		self.create_player()
		map, biome_map = self.load_map()
		eval(PRINT_SEPARATER)
		self.Player.describe_spawnpoint(self)
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
		print("NewScript version 0.6")
		print("Type 'help' for the command list.")
		while True:
			self.command_input()
		
	
if __name__ == "__main__": NewScript = Game()
