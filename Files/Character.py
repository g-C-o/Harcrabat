"""
Character.py
NewScript
"""

from Database import MOVE_DELAY, COLLECT_DELAY, PRINT_COLORS
from time import time
from colorama import Style
from ColPrint import colprint


class Character:
	def __init__(self, name, score, map, biome_map, collect_time_map,  health, energy, inventory, items, hand_item, hand_item_slot, armor, location, orientation, last_move_time, reference):
		self.name = name
		self.score = score
		self.map = map
		self.biome_map = biome_map
		self.collect_time_map = collect_time_map
		self.health = health
		self.energy = energy
		self.inventory = inventory
		self.items = items
		self.hand_item = hand_item
		self.hand_item_slot = hand_item_slot
		self.armor = armor
		self.location = location
		self.orientation = orientation
		self.last_move_time = last_move_time
		self.reference = reference

		while len(self.items) <= 9:
			self.items.append(None)

	def craft(self, game):
		# Check for item:
		desired_item = input("Craft: ")
		try:
			# eval("game." + desired_item + ".recipe")
			desired_item_recipe = self.reference[desired_item].recipe
		except KeyError:
			print("That item does not exist")
			return
		can_craft_item = True

		# Check for ingredients:
		# print(desired_item_recipe)
		for item in desired_item_recipe:
			item_obj = eval("game." + item)
			amount = desired_item_recipe[item]
			if item_obj not in self.inventory or self.inventory[item_obj] < amount:
				print("You cannot craft this item")
				return
			else:
				self.inventory[item_obj] -= amount

		# Craft item:
		desired_item_obj = self.reference[desired_item]
		try:
			self.inventory[desired_item_obj] += 1
		except KeyError:
			self.inventory[desired_item_obj] = 1
		print("You crafted 1", desired_item_obj.name)

	def look(self, game):
		try:
			if self.orientation == "North":
				biome_ahead = self.biome_map[self.location[0] -
											 1][self.location[1]].name
			elif self.orientation == "South":
				biome_ahead = self.biome_map[self.location[0] -
											 1][self.location[1]-1].name
			elif self.orientation == "West":
				biome_ahead = self.biome_map[self.location[0]
											 ][self.location[1]-1].name
			elif self.orientation == "East":
				biome_ahead = self.biome_map[self.location[0]
											 ][self.location[1]-1].name
			for Index, Coord in enumerate(self.location):
				if Coord < 0 or Coord > 50:
					raise IndexError
			article = eval("game." + biome_ahead).preposition[5:]
			print("You look %s and see %s %s." %
				  (self.orientation, article, biome_ahead))
		except IndexError:
			print("You see the edge of the world.")

	def describe_spawnpoint(self, game):
		current_biome = self.biome_map[26][26].name
		alt_preposition = eval(
			"game." + current_biome).preposition[:2] + eval("game." + current_biome).preposition[4:]
		print("You spawn %s %s%s%s. You are facing North." % (alt_preposition, PRINT_COLORS[eval(
			"game." + current_biome).rarity], current_biome, PRINT_COLORS["Reset"]))

	def describe_surroundings(self, game):
		current_biome = self.biome_map[self.location[0]][self.location[1]].name
		current_env = self.map[self.location[0]][self.location[1]]
		print("Current Location:")
		print("\tCoordinates: " + str(self.location))
		print("\tEnvironment: " + current_env)
		print("\tBiome: " + PRINT_COLORS[eval(
			"game." + current_biome).rarity] + current_biome + PRINT_COLORS["Reset"])

	def set_name(self, new_name):
		self.name = new_name

	def switch_hand_item(self, new_item):
		if new_item != None:
			self.hand_item = new_item
			print("Hand item switched to", new_item.name)
		else:
			if self.hand_item != None:
				self.hand_item = None
				print("You have switched to your bare hand.")

	def switch_armor(self, new_armor):
		self.armor = new_armor

	def move(self, game):
		if time() - self.last_move_time < MOVE_DELAY:
			return
		try:
			if self.orientation == "North":
				self.location[0] -= 1
			elif self.orientation == "South":
				self.location[0] += 1
			elif self.orientation == "West":
				self.location[1] -= 1
			elif self.orientation == "East":
				self.location[1] += 1
			for index, coord in enumerate(self.location):
				if coord < 0:
					self.location[index] = 0
				elif coord > 50:
					self.location[index] = 50
				else:
					continue
				raise IndexError
			current_biome = self.biome_map[self.location[0]
										   ][self.location[1]].name
			self.last_move_time = time()
			print("You move %s %s" % (self.orientation, eval(
				"game." + current_biome).preposition), end=" ")
			print(PRINT_COLORS[eval("game." + current_biome).rarity] +
				  current_biome + PRINT_COLORS["Reset"], end=".\n")
		except IndexError:
			print("You have reached the edge of the world.")

	def turn(self, new_orientation):
		self.orientation = new_orientation
		print("You turn to the %s." % new_orientation)

	def collect(self):
		if time() - self.collect_time_map[self.location[0]][self.location[1]] < COLLECT_DELAY:
			return
		NewResources = self.biome_map[self.location[0]
									  ][self.location[1]].gen_resources()
		self.collect_time_map[self.location[0]][self.location[1]] = time()
		print("You harvested new resources:")
		displayed_resources = []
		for NewResource in NewResources:
			try:
				self.inventory[NewResource] += 1
			except KeyError:
				self.inventory[NewResource] = 1
			if NewResource in displayed_resources:
				continue
			else:
				displayed_resources.append(NewResource)
				if NewResources.count(NewResource) == 1:
					resource_name = NewResource.name
				else:
					resource_name = NewResource.plural
				print("\t%i %s%s" % (NewResources.count(
					NewResource), PRINT_COLORS[NewResource.rarity], resource_name) + Style.RESET_ALL)

	def attack(self):
		if self.hand_item == None:
			print("You punch with your bare hand at thin air.")
		elif not self.hand_item.is_weapon:
			print("You cannot attack with the selected item.")
		else:
			self.hand_item.attack(None)
			if self.hand_item.expendable:
				self.hand_item = None
				self.items[hand_item_slot] = None

	def moveItem(self):
		while True:
			tof = input(
				"Would you like to move an item to your hotbar or from your hotbar?\nPlease input to (t) or from (f): ")
			if tof == "from" or "f" in tof:
				toHotbar = False
				break
			elif tof == "to" or "t" in tof:
				toHotbar = True
				break
			print("Sorry. Please input a valid response.")
		item_to_move = input("Item to move: ")
		if item_to_move == "Fists" or item_to_move == "Arm":
			print("Sorry. You cannot move this item to your inventory.")
			return
		try:
			item_object = self.reference[item_to_move]
		except KeyError:
			print("Sorry. That item does not exist.")
			return
		if toHotbar:
			if item_object in self.inventory.keys():
				while True:
					try:
						slotNum = int(input("Slot to move to: "))
						if slotNum <= 9 and slotNum >= 0:
							break
					except:
						pass

					print("Sorry. Please input a valid slot between 0 and 9.")

				if self.items[slotNum] != None:
					if self.items[slotNum] in self.inventory.keys():
						self.inventory[self.items[slotNum]] += 1
					else:
						self.inventory[self.items[slotNum]] = 1
					print("1", self.items[slotNum].name, "moved to inventory")
				self.inventory[item_object] -= 1
				self.items[slotNum] = item_object
				print("1", item_to_move, "moved to hotbar")

			else:
				print("Sorry. That item is not in your inventory.")

		else:
			if item_object in self.items:
				itemIndex = self.items.index(item_object)
				self.items[itemIndex] = None
				print("1", item_to_move, "added to inventory.")
				if self.hand_item_slot == itemIndex:
					self.switch_hand_item(None)
				if item_object in self.inventory.keys():
					self.inventory[item_object] += 1
				else:
					self.inventory[item_object] = 1

			else:
				print("Sorry. That item is not in your hotbar.")

	def list_inv(self):
		"""print("Inventory:")
		for Resource in self.inventory:
						if self.inventory[Resource] == 1:
										resource_name = Resource.name
						else:
										resource_name = Resource.plural
						print("\t" + str(self.inventory[Resource]) + " " +
										  PRINT_COLORS[Resource.rarity] + resource_name + PRINT_COLORS["Reset"])

		print("\nHotbar:")
		for slot, item in enumerate(self.items):
						if item != None:
										resource_name = item.name
										print("\t" + " " + str(slot) + " " +
														PRINT_COLORS[item.rarity] + resource_name + PRINT_COLORS["Reset"])
						else:
										print("\t" + " " + str(slot))"""

		# New Print Style
		invList = []
		for Resource in self.inventory.keys():
			if self.inventory[Resource] == 1:
				resource_name = Resource.name
			else:
				resource_name = Resource.plural
			invList.append(str(self.inventory[Resource]) + " " +
						   PRINT_COLORS[Resource.rarity] + resource_name + PRINT_COLORS["Reset"])
		if len(invList) == 0:
			invList.append("")
		itemList = []
		for slot, item in enumerate(self.items):
			if item != None:
				resource_name = item.name
				itemList.append(str(slot) + " " +
								PRINT_COLORS[item.rarity] + resource_name + PRINT_COLORS["Reset"])
			else:
				itemList.append(str(slot))

		colprint(["Inventory:", "Hotbar:"], invList, itemList)
