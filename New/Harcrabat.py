"""
Harcrabat Version 0.9
A text-based game of collecting, crafting, and killing
Made by Cameron White & Dallin Guisti
Optimized for python 3.6 & 3.7
"""

from Database import *
from Player import Player
import Item
import Environment
from random import choices
from colorama import Fore, Back, init, Style
from time import time, sleep
import msvcrt


### START CODE ###


class Game:

	
	def __init__(self):
	
		self.last_spawn_time = time()
		self.mob_map = [[None for square in range(51)] for row in range(51)]
		self.initial_mobs_spawned = False

		self.items = []
		for item in ITEM_NAMES:
			item_obj = eval("Item." + item)
			self.items.append(item_obj)
		
		self.environments = []
		for environment in ENVIRONMENT_NAMES:
			environment_obj = eval("Environment." + environment)
			self.environments.append(environment_obj)
		self.startup()


	### GAME FUNCTIONS ###
	

	def create_player(self):
		collect_map = [[time() - COLLECT_DELAY for square in range(51)] for row in range(51)]
		inventory = {item: 0 for item in self.items}
		self.User = Player("Player1", 0, [], [], collect_map, 100, 100, inventory, None, None, [26,26], "North", time())
		
	def choose_environment(self, surroundings):
		surroundings = [Square for Square in surroundings if Square] 
		env_probs = {Env().type: ENV_INCONSISTENCY for Env in self.environments}
		for Square in surroundings:
			square_type = Square.type
			env_probs [square_type] = env_probs [square_type] * ENV_CLUSTER_SIZE
		env_weights = [prob for prob in list(env_probs.values())]
		EnvChoice = choices(self.environments, weights=env_weights)[0]()
		return EnvChoice


	def choose_biome(self, Env):
		BiomeChoice = choices([Env.pri_B, Env.sec_B, Env.ter_B, Env.structure], weights=BIOME_WEIGHTS)[0]
		NewBiome = BiomeChoice()
		return NewBiome

	
	def load_game_map(self):
		print("Loading map")

		## Preload self.game_map:
		print("\tCreating Seed")
		self.game_map = [[None 
				if col_index in [0,52]
				or row_index in [0,52]
				else choices(self.environments)[0]()
			for col_index in range(53)]
			for row_index in range(53)]
		
		## Choose Environments:
		print("\tGenerating Chunks")
		for rep in range(ENV_CLEANUP_FACTOR):
			self.game_map = [[None
					if col_index in [0,52]
					or row_index in [0,52]
					else self.choose_environment([self.game_map[row_index-1][col_index-1], self.game_map[row_index-1][col_index], self.game_map[row_index-1][col_index+1], self.game_map[row_index][col_index-1], self.game_map[row_index][col_index+1], self.game_map[row_index+1][col_index-1], self.game_map[row_index+1][col_index], self.game_map[row_index+1][col_index+1]])
				for col_index in range(len(self.game_map[row_index]))]
				for row_index in range(len(self.game_map))]
		self.game_map = [[Env for Env in row[1:-1]] for row in self.game_map[1:-1]]

		## Choose Biomes:
		print("\tGenerating Terrain")
		self.biome_map = [[self.choose_biome(Env)
			for Env in row]
			for row in self.game_map]


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
			self.mob_map = Mob.spawn_initial_mobs(self.mob_map, self.Player.self.biome_map)
			self.initial_mobs_spawned = True
			self.last_spawn_time = time()
		elif time() - self.last_spawn_time >= MOB_REPLACE_DELAY:
			self.mob_map = Mob.replace_mobs(self.mob_map, self.Player.self.biome_map)
			self.last_spawn_time = time()
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
		#### Update health and energy
		#### Regenerate resources in exhausted squares
		#### Spawn Animals


	### COMMAND FUNCTIONS ###


	def help(self):
		[print(command + ": " + COMMANDS[command]) for command in COMMANDS]


	def start(self):
		self.create_player()
		self.load_game_map()
		eval(PRINT_SEPARATER)
		self.User.describe_spawnpoint(self.biome_map)
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

	
	def run_program(self):
		while True:
			self.command_input()


	def startup(self):
		init() # For color-printing mechanism
		print(STARTUP_MESSAGE)
		print("Type 'help' for the command list.")
		self.run_program()
		
	
if __name__ == "__main__": NewScript = Game()
