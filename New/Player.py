"""
Character.py
Harcrabat
"""

from Database import MOVE_DELAY, COLLECT_DELAY, PRINT_COLORS
from time import time
from colorama import Style


class Player:
	def __init__(self, name, score, game_map, biome_map, collect_time_map, health, energy, inventory, hand_item, armor, location, orientation, last_move_time):
		self.name = name
		self.score = score
		self.game_map = game_map
		self.biome_map = biome_map
		self.collect_time_map = collect_time_map
		self.health = health
		self.energy = energy
		self.inventory = inventory
		self.hand_item = hand_item
		self.armor = armor
		self.location = location
		self.orientation = orientation
		self.last_move_time = last_move_time
		
	
	def craft(self):
		## Check for item:
		desired_item = input("Craft: ")
		for item in self.inventory:
			if item.name == desired_item:
				desired_item_recipe = item.recipe
				desired_item_obj = item
		try: desired_item_recipe
		except NameError:
			print ("That item does not exist")
			return #### return print function?
		
		## Check for ingredients:
		for req_item in desired_item_recipe:
			amount = desired_item_recipe[req_item]
			if self.inventory[req_item] < amount:
				print ("You cannot craft this item")
				return #### Same as above
			else: self.inventory [req_item] -= amount
		
		## Craft item:
		self.inventory [desired_item_obj] += 1
		print ("You crafted 1", desired_item_obj.name)
			
			
		
	
	
	def look(self):
		## Find Biome ahead
		try:
			if self.orientation  == "North":
				biome_ahead = self.biome_map [self.location[0]-1][self.location[1]] 
			elif self.orientation  == "South":
				biome_ahead = self.biome_map [self.location[0]+1][self.location[1]]
			elif self.orientation  == "West":
				biome_ahead = self.biome_map [self.location[0]][self.location[1]-1] 
			elif self.orientation  == "East":
				biome_ahead = self.biome_map [self.location[0]][self.location[1]+1] 
			for Index, Coord in enumerate(self.location):
				if Coord < 0 or Coord > 50:
					raise IndexError
					
			## Print Biome ahead
			article = biome_ahead.preposition[5:]
			print("You look %s and see %s %s." %(self.orientation, article, biome_ahead.name))			
		except IndexError:
			print("You see the edge of the world.")

		
	def describe_spawnpoint(self, biome_map):
		current_biome = biome_map[26][26]
		alt_preposition = current_biome.preposition[:2] + current_biome.preposition[4:]
		print("You spawn %s %s%s%s. You are facing North." % (alt_preposition, PRINT_COLORS[current_biome.rarity], current_biome.name, PRINT_COLORS["Reset"]))


	def describe_surroundings(self):
		current_biome = self.biome_map [self.location[0]][self.location[1]] # Is an object
		current_env = self.game_map [self.location[0]][self.location[1]] # Is a string
		print("Current Location:")
		print("\tCoordinates: " + str(self.location))
		print("\tEnvironment: " + current_env)
		print("\tBiome: " + PRINT_COLORS[current_biome.rarity] + current_biome.name + PRINT_COLORS["Reset"])


	def switch_hand_item(self, new_item):
		self.hand_item = new_item

		
	def switch_armor(self, new_armor):
		self.armor = new_armor

	
	def move(self, mob_map):
		if time() - self.last_move_time < MOVE_DELAY: return
		try:
			if self.orientation  == "North":
				self.location [0] -= 1
			elif self.orientation  == "South":
				self.location [0] += 1
			elif self.orientation  == "West":
				self.location [1] -= 1
			elif self.orientation  == "East":
				self.location [1] += 1
			for index, coord in enumerate(self.location):
				if coord < 0:
					self.location [index] = 0
				elif coord > 50:
					self.location [index] = 50
				else: continue
				raise IndexError
			current_biome = self.biome_map [self.location[0]][self.location[1]]
			self.last_move_time = time()
			print("You move %s %s" %(self.orientation, current_biome.preposition), end=" ")
			print (PRINT_COLORS[current_biome.rarity] + current_biome.name + PRINT_COLORS["Reset"], end=".\n")
		except IndexError:
			print("You have reached the edge of the world.")


	def turn(self, new_orientation):
		self.orientation = new_orientation
		print("You turn to the %s." % new_orientation)


	def collect(self):
		if time() - self.collect_time_map [self.location [0]] [self.location [1]] < COLLECT_DELAY: return
		NewResources = self.biome_map [self.location[0]][self.location[1]].gen_resources()
		self.collect_time_map [self.location [0]] [self.location [1]] = time()
		print("You harvested new resources:")
		displayed_resources = []
		for NewResource in NewResources:
			try: self.inventory [NewResource] += 1
			except KeyError: self.inventory [NewResource] = 1
			if NewResource in displayed_resources: continue
			else:
				displayed_resources.append(NewResource)
				if NewResources.count(NewResource) == 1:
					resource_name = NewResource.name
				else: resource_name = NewResource.plural
				print("\t%i %s%s" %(NewResources.count(NewResource), PRINT_COLORS[NewResource.rarity], resource_name) + Style.RESET_ALL)
		

	def attack(self):
		print("attack")


	def list_inv(self):
		print("Inventory:")
		for Resource in self.inventory:
			if self.inventory [Resource] == 0:
				continue
			elif self.inventory [Resource] == 1:
				resource_name = Resource.name
			else: resource_name = Resource.plural
			print("\t" + str(self.inventory[Resource]) + " " + PRINT_COLORS[Resource.rarity] + resource_name + PRINT_COLORS["Reset"])
