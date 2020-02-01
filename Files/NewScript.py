"""
NewScript Version 0.8
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
from time import time
import msvcrt
from FileSystem import FileSystem, SC_ERRORS
import traceback
import sys
from inspect import currentframe, getframeinfo


### START CODE ###


class Game:

	def __init__(self):
		self.Character = Character
		self.Resource = Resource
		self.Item = Item
		self.Mob = Mob
		self.Animal = Animal
		self.Biome = Biome
		self.Environment = Environment
		self.Weapon = Weapon
		self.Projectile = Projectile

		# Resources:
		if True:
			self.Rec_Ref = {}
			self.Soil = self.Resource("Soil Pile", "Common", self.Rec_Ref)
			self.Wood = self.Resource("Wood Block", "Common", self.Rec_Ref)
			self.Vine = self.Resource("Vine", "Common", self.Rec_Ref)
			self.Fruit = self.Resource("Fruit", "Common", self.Rec_Ref)
			self.Rock = self.Resource("Rock", "Common", self.Rec_Ref)
			self.Water = self.Resource("Water Supply", "Common", self.Rec_Ref)
			self.Sand = self.Resource("Sand Pile", "Common", self.Rec_Ref)
			self.Cacti = self.Resource("Cacti Block", "Common", self.Rec_Ref)
			self.Iron = self.Resource("Iron Nugget", "Uncommon", self.Rec_Ref)
			self.Bone = self.Resource("Bone", "Common", self.Rec_Ref)
			self.Diamond = self.Resource("Diamond", "Uncommon", self.Rec_Ref)
			self.Stone = self.Resource("Stone", "Common", self.Rec_Ref)
			self.Gold = self.Resource("Gold Nugget", "Uncommon", self.Rec_Ref)
			self.Emerald = self.Resource("Emerald", "Uncommon", self.Rec_Ref)
			self.Quartz = self.Resource("Quartz Shard", "Uncommon", self.Rec_Ref)
			self.Explosive = self.Resource("Explosive", "Common", self.Rec_Ref)

		# Items:
		if True:
			self.HarvesterArmor = self.Item("Harvester's Armor", None, "Rare", self.Rec_Ref)
			self.Protector = self.Item("Protector", None, "Legendary", self.Rec_Ref)
			self.Strawman = self.Item("Strawman", None, "Rare", self.Rec_Ref)
			self.Coffin = self.Item("Coffin", None, "Legendary", self.Rec_Ref)
			self.Ladder = self.Item("Ladder", None, "Rare", self.Rec_Ref)
			self.MobRepellant = self.Item("Mob Repellent", None, "Legendary", self.Rec_Ref)
			self.BottledWave = self.Item("Bottled Wave", None, "Rare", self.Rec_Ref)
			self.BottledWind = self.Item("Bottled Wind", None, "Legendary", self.Rec_Ref)
			self.Glider = self.Item("Glider", None, "Rare", self.Rec_Ref)
			self.Binoculars = self.Item("Binoculars", None, "Legendary", self.Rec_Ref)

		# Projectiles:
		if True:
			self.WoodenBall = self.Projectile(
				"Wooden Ball", {"Wood": 5}, ["Arm"], 13, "Common", self.Rec_Ref)
			self.StoneBall = self.Projectile(
				"Stone Ball", {"Wood": 5, "Stone": 2}, ["Arm"], 15, "Common", self.Rec_Ref)
			self.IronBall = self.Projectile(
				"Iron Ball", {"Wood": 5, "IronIngot": 2}, ["Arm"], 17, "Common", self.Rec_Ref)
			self.DiamondBall = self.Projectile(
				"Diamond Ball", {"Wood": 5, "Diamond": 2}, ["Arm"], 25, "Uncommon", self.Rec_Ref)
			self.WoodenArrow = self.Projectile("Wooden Arrow", {"Wood": 3}, [
											"Bow", "CrossBow"], 17, "Common", self.Rec_Ref)
			self.StoneArrow = self.Projectile("Stone Arrow", {"Stone": 2, "Wood": 3}, [
											"Bow", "CrossBow"], 20, "Common", self.Rec_Ref)
			self.IronArrow = self.Projectile("Iron Arrow", {"IronIngot": 1, "Wood": 3}, [
											"Bow", "CrossBow"], 23, "Common", self.Rec_Ref)
			self.DiamondArrow = self.Projectile("Diamond Arrow", {"Diamond": 1, "Wood": 3}, [
												"Bow", "CrossBow"], 26, "Uncommon", self.Rec_Ref)
			self.SoilClump = self.Projectile("Soil Clump", {"Soil": 4}, [
											"CombatBucket"], 38, "Common", self.Rec_Ref)
			self.SandClump = self.Projectile("Sand Clump", {"Sand": 4}, [
											"CombatBucket"], 38, "Common", self.Rec_Ref)
			self.CactusClump = self.Projectile("Cactus Clump", {"Cacti": 2}, [
											"CombatBucket"], 55, "Common", self.Rec_Ref)
			self.WoodSpike = self.Projectile("Wood Spike", {"Wood": 2}, [
											"Slingshot"], 17, "Common", self.Rec_Ref)
			self.StoneSpike = self.Projectile("Stone Spike", {"Stone": 3}, [
											"Slingshot"], 19, "Common", self.Rec_Ref)
			self.IronSpike = self.Projectile("Iron Spike", {"IronIngot": 1, "Wood": 1}, [
											"Slingshot"], 21, "Common", self.Rec_Ref)
			self.DiamondSpike = self.Projectile(
				"Diamond Spike", {"Diamond": 1, "Wood": 1}, ["Slingshot"], 26, "Uncommon", self.Rec_Ref)
			self.CannonBall = self.Projectile(
				"Cannon Ball", {"Wood": 10, "Stone": 15}, ["Cannon"], 125, "Common", self.Rec_Ref)
			self.Rocket = self.Projectile("Rocket", {"Iron": 15, "Explosive": 5}, [
										"RocketLauncher"], 150, "Rare", self.Rec_Ref)
			self.Missile = self.Projectile("Missile", {"Iron": 15, "Explosive": 10}, [
										"MissileLauncher"], 200, "Rare", self.Rec_Ref)

		# Weapons:
		if True:
			self.Arm = self.Weapon("Arm", None, "Range", 1,
								90, None, 2, False, "Common", "swing", "swung", self.Rec_Ref)
			self.Bow = self.Weapon(
				"Bow", {"Wood": 8, "Vine": 1}, "Range", 1.25, 60, None, 3, False, "Common", "shoot", "shot", self.Rec_Ref)
			self.Crossbow = self.Weapon(
				"Crossbow", {"Wood": 10, "Vine": 2}, "Range", 1.25, 60, None, 3, True, "Common", "fire", "fires", self.Rec_Ref)
			self.CombatBucket = self.Weapon("Combat Bucket", {
											"IronIngot: 12"}, "Range", 1.75, 100, None, 0, False, "Uncommon", "swing", "swung", self.Rec_Ref)
			self.Slingshot = self.Weapon(
				"Slingshot", {"Wood": 8, "Vine": 1}, "Range", 0.75, 90, None, 1, False, "Common", "fire", "fired", self.Rec_Ref)
			self.Cannon = self.Weapon("Cannon", {
									"Iron": 1, "Wood": 200, "Explosive": 2}, "Range", 10, 100, None, 1, False, "Uncommon", "fire", "fired", self.Rec_Ref)
			self.RocketLauncher = self.Weapon("Rocket Launcher", {
											"Iron": 20, "Stone": 185, "Wood": 15, "Explosive": 6}, "Range", 25, 100, None, 6, True, "Rare", "fire", "fired", self.Rec_Ref)
			self.MissileLauncher = self.Weapon("Missile Launcher", {
											"Iron": 50, "Stone": 200, "Wood": 50, "Explosive": 8}, "Range", 40, 100, None, 8, True, "Legendary", "fire", "fired", self.Rec_Ref)
			self.Fists = self.Weapon("Fists", None, "Melee", 0.5,
									100, 5, 0, None, "Common", "punch", "punched", self.Rec_Ref)
			self.BoneBlade = self.Weapon(
				"Bone Blade", {"Bone": 3}, "Melee", 1.25, 90, 10, 0, None, "Common", "swing", "swung", self.Rec_Ref)
			self.BoneStriker = self.Weapon(
				"Bone Striker", {"Bone": 8}, "Melee", 1.25, 90, 25, 0, None, "Uncommon", "strike", "struck", self.Rec_Ref)
			self.WoodenSword = self.Weapon(
				"Wooden Sword", {"Wood": 8}, "Melee", 1, 80, 17, 0, None, "Common", "swing", "swung", self.Rec_Ref)
			self.StoneSword = self.Weapon(
				"Stone Sword", {"Stone": 10, "Wood": 3}, "Melee", 1, 80, 20, 0, None, "Common", "swing", "swung", self.Rec_Ref)
			self.IronSword = self.Weapon("Iron Sword", {
										"IronIngot": 10, "Wood": 3}, "Melee", 1, 80, 23, 0, None, "Uncommon", "swing", "swung", self.Rec_Ref)
			self.DiamondSword = self.Weapon(
				"Diamond Sword", {"Diamond": 10, "Wood": 3}, "Melee", 1, 80, 26, 0, None, "Rare", "swing", "swung", self.Rec_Ref)
			self.WoodenAxe = self.Weapon(
				"Wooden Axe", {"Wood": 9}, "Melee", 1.5, 70, 26, 0, None, "Common", "swing", "swung", self.Rec_Ref)
			self.StoneAxe = self.Weapon(
				"Stone Axe", {"Stone": 10, "Wood": 4}, "Melee", 1.5, 70, 30, 0, None, "Common", "swing", "swung", self.Rec_Ref)
			self.IronAxe = self.Weapon("Iron Axe", {
									"IronIngot": 10, "Wood": 4}, "Melee", 1.5, 70, 34, 0, None, "Uncommon", "swing", "swung", self.Rec_Ref)
			self.DiamondAxe = self.Weapon(
				"Diamond Axe", {"Diamond": 10, "Wood": 4}, "Melee", 1.5, 70, 38, 0, None, "Rare", "swing", "swung", self.Rec_Ref)
			self.WoodenSpear = self.Weapon(
				"Wooden Spear", {"Wood": 10}, "Melee", 1.75, 60, 30, 1, None, "Common", "throw", "threw", self.Rec_Ref)
			self.StoneSpear = self.Weapon(
				"Stone Spear", {"Stone": 10, "Wood": 5}, "Melee", 1.75, 60, 35, 1, None, "Common", "throw", "threw", self.Rec_Ref)
			self.IronSpear = self.Weapon("Iron Spear", {
										"IronIngot": 10, "Wood": 5}, "Melee", 1.75, 60, 40, 1, None, "Uncommon", "throw", "threw", self.Rec_Ref)
			self.DiamondSpear = self.Weapon("Diamond Spear", {
											"Diamond": 10, "Wood": 5}, "Melee", 1.75, 60, 45, 1, None, "Rare", "throw", "threw", self.Rec_Ref)
			self.WoodenBoomerang = self.Weapon(
				"Wooden Boomerang", {"Wood": 12}, "Melee", 3, 90, 40, 2, None, "Common", "throw", "threw", self.Rec_Ref)
			self.StoneBoomerang = self.Weapon("Stone Boomerang", {
											"Stone": 10, "Wood": 6}, "Melee", 3, 90, 50, 2, None, "Common", "throw", "threw", self.Rec_Ref)
			self.IronBoomerang = self.Weapon("Iron Boomerang", {
											"IronIngot": 10, "Wood": 6}, "Melee", 3, 90, 60, 2, None, "Uncommon", "throw", "threw", self.Rec_Ref)
			self.DiamondBoomerang = self.Weapon("Diamond Boomerang", {
												"Diamond": 10, "Wood": 6}, "Melee", 3, 90, 70, 2, None, "Rare", "throw", "threw", self.Rec_Ref)
			self.Bomb = self.Weapon("Bomb", {
									"Stone": 25, "Wood": 25, "Explosive": 5}, "Melee", 15, 100, 100, 0, None, "Common", "explode", "exploded", self.Rec_Ref, expendable=True)
			self.Grenade = self.Weapon("Grenade", {
									"Stone": 4, "Wood": 4, "Explosive": 2}, "Melee", 8, 100, 75, 0, None, "Common", "throw", "threw", self.Rec_Ref)
			self.Dynamite = self.Weapon(
				"Dynamite", {"Explosive": 1}, "Melee", 1, 100, 50, None, False, "Common", "throw", "threw", self.Rec_Ref)

		# Player:
		self.Player = self.Character(None, 0, [], [], [[time() - COLLECT_DELAY for square in range(51)]
													   for row in range(50)], 100, 100, {}, [self.Fists], None, 0, None, [26, 26], "North", time(), self.Rec_Ref)
  
		# Mobs:
		if True:
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

		# Animals:
		if True:
			self.Chicken = self.Animal()
			self.Rabbit = self.Animal()
			self.Cow = self.Animal()
			self.Fish = self.Animal()
			self.Sheep = self.Animal()

		# Biomes:
		if True:
			self.Forest = self.Biome("Forest", "into a", self.Wood, self.Soil, self.Soil,
									self.Fighter, self.Fighter, self.Fighter, self.Chicken, None, None, "Common")
			self.Jungle = self.Biome("Jungle", "into a", self.Wood, self.Soil, self.Emerald,
									self.Fighter, self.Fighter, self.Predator, self.Chicken, None, None, "Uncommon")
			self.Grove = self.Biome("Grove", "into a", self.Wood, self.Fruit, self.Emerald,
									self.Fighter, self.Predator, self.Fighter, self.Chicken, None, None, "Rare")
			self.Garden = self.Biome("Garden", "into a", self.Wood, self.Emerald, self.Gold, self.Fighter,
									self.Predator, self.Goblin, self.Chicken, self.HarvesterArmor, self.Protector, "Legendary")
			self.Desert = self.Biome("Desert", "into a", self.Sand, self.Stone, self.Stone,
									self.Destroyer, self.Destroyer, self.Destroyer, self.Rabbit, None, None, "Common")
			self.Tundra = self.Biome("Tundra", "into a", self.Sand, self.Stone, self.Iron,
									self.Destroyer, self.Destroyer, self.Annihilator, self.Rabbit, None, None, "Uncommon")
			self.Badland = self.Biome("Badland", "into a", self.Sand, self.Cacti, self.Iron,
									self.Destroyer, self.Annihilator, self.Destroyer, self.Rabbit, None, None, "Rare")
			self.Temple = self.Biome("Temple", "into a", self.Sand, self.Iron, self.Diamond, self.Destroyer,
									self.Annihilator, self.Troll, self.Rabbit, self.Strawman, self.Coffin, "Legendary")
			self.Prairie = self.Biome("Prairie", "into a", self.Soil, self.Water, self.Water,
									self.Raider, self.Raider, self.Raider, self.Cow, None, None, "Common")
			self.Meadow = self.Biome("Meadow", "into a", self.Soil, self.Water, self.Diamond,
									self.Raider, self.Raider, self.Minion, self.Cow, None, None, "Uncommon")
			self.Swamp = self.Biome("Swamp", "into a", self.Soil, self.Vine, self.Diamond,
									self.Raider, self.Minion, self.Raider, self.Cow, None, None, "Rare")
			self.Fort = self.Biome("Fort", "into a", self.Soil, self.Diamond, self.Iron, self.Raider,
								self.Minion, self.Zombie, self.Cow, self.Ladder, self.MobRepellant, "Legendary")
			self.Lake = self.Biome("Lake", "into a", self.Water, self.Sand, self.Water,
								self.Defender, self.Defender, self.Defender, self.Fish, None, None, "Common")
			self.Beach = self.Biome("Beach", "into a", self.Water, self.Sand, self.Diamond,
									self.Defender, self.Defender, self.Guardian, self.Fish, None, None, "Uncommon")
			self.Island = self.Biome("Island", "onto an", self.Water, self.Bone, self.Diamond,
									self.Defender, self.Guardian, self.Defender, self.Fish, None, None, "Rare")
			self.Shipwreck = self.Biome("Shipwreck", "into a", self.Water, self.Gold, self.Quartz, self.Defender,
										self.Guardian, self.Skeleton, self.Fish, self.BottledWave, self.BottledWind, "Legendary")
			self.Mountain = self.Biome("Mountain", "onto a", self.Stone, self.Wood, self.Sand,
									self.Hunter, self.Hunter, self.Hunter, self.Sheep, None, None, "Common")
			self.Canyon = self.Biome("Canyon", "into a", self.Stone, self.Wood, self.Gold,
									self.Hunter, self.Hunter, self.Assasin, self.Sheep, None, None, "Uncommon")
			self.Cave = self.Biome("Cave", "into a", self.Stone, self.Explosive, self.Gold,
								self.Hunter, self.Assasin, self.Hunter, self.Sheep, None, None, "Rare")
			self.Monument = self.Biome("Monument", "into a", self.Stone, self.Gold, self.Iron, self.Hunter,
									self.Assasin, self.Ghoul, self.Sheep, self.Glider, self.Binoculars, "Legendary")

		# Environments:
		if True:
			self.Woodlands = self.Environment(
				self.Forest, self.Jungle, self.Grove, self.Garden)
			self.Plains = self.Environment(
				self.Desert, self.Tundra, self.Badland, self.Temple)
			self.Grasslands = self.Environment(
				self.Prairie, self.Meadow, self.Swamp, self.Fort)
			self.Waterlands = self.Environment(
				self.Lake, self.Beach, self.Island, self.Shipwreck)
			self.Rockylands = self.Environment(
				self.Mountain, self.Canyon, self.Cave, self.Monument)

		self.startup()

	### GAME FUNCTIONS ###

	def create_player(self):
		if self.Player.name == None:
			desired_name = input("Enter your name:\n| ")
			if desired_name != "":
				self.Player.set_name(desired_name)
		else:
			print("Welcome back,", self.Player.name + "!")
		eval(PRINT_SEPARATER)

	def save(self):
		if self.Player.name == None:
			self.filesystem.save({"inventory": self.Player.inventory})
		else:
			self.filesystem.save({"inventory": self.Player.inventory, "plyrinfo": {"name": self.Player.name}})

	def load_map(self):
		print("Loading map")

		## Preload map:
		print("\tCreating Seed")
		map = [[None 
				if col_index in [0,52]
				or row_index in [0,52]
				else choices(("Woodlands", "Plains", "Grasslands", "Waterlands", "Rockylands"))[0]
			for col_index in range(53)]
			for row_index in range(53)]
		
		## Choose Environments:
		print("\tGenerating Chunks")
		for rep in range(ENV_CLEANUP_FACTOR):
			map = [[None
					if col_index in [0,52]
					or row_index in [0,52]
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

	def switch_item(self, item_number):
		if self.Player.hand_item_slot != item_number:
			if len(self.Player.items) - 1 >= item_number:
				self.Player.switch_hand_item(self.Player.items[item_number])
				self.Player.hand_item_slot = item_number
			else:
				if self.Player.hand_item != None:
					self.Player.switch_hand_item(None)
				self.Player.hand_item_slot = item_number
 
	def run_game(self):
		# Wait for keypress:
		while True:
			while not msvcrt.kbhit():
				pass
				# Update game
			key_input = msvcrt.getch()

			# Respond to keypress:
			if key_input in KEY_BINDINGS:
				eval(KEY_BINDINGS[key_input][0])

	def update_game(self):
		# Update health and energy
		# Regenerate resources in exhausted squares
		# Spawn stuff
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
		quit()

	def controls(self):
		for key in KEY_BINDINGS:
			if key == b" ":
				letter = "SPACE"
			else:
				letter = key.decode("utf-8")
			print(letter + ": " + KEY_BINDINGS[key][1])

	### MANAGER FUNCTIONS ###

	def command_input(self):
		eval(PRINT_SEPARATER)
		command = (input("| ")).lower()
		eval(PRINT_SEPARATER)
		if command in COMMANDS:
			eval("self." + command + "()")
		else:
			print("Invalid Command")

	def startup(self):
		init()
  
		# Import player save data
		print("Loading save data...")
		self.filesystem = FileSystem("..\\Savefiles\\")
  
		#frameinfo = getframeinfo(currentframe())
		#self.filesystem.error(SC_ERRORS.test, frameinfo.filename + " " + str(frameinfo.lineno-3), info="This is a test for the NewScript error system.")
		
		print("NewScript version 0.8")
  
		data = self.filesystem.load()
		if "inventory" in data.keys():
			for item, amount in data["inventory"]:
				itemID = self.Rec_Ref[item]
				self.Player.inventory[itemID] = int(amount)
		if "plyrinfo" in data.keys():
			if "name" in data["plyrinfo"].keys():
				self.Player.set_name(data["plyrinfo"]["name"])

		print("Type 'help' for the command list.")
		while True:
			self.command_input()


if __name__ == "__main__":
	NewScript = Game()