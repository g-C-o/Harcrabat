"""
Item.py
Harcrabat
"""



### ITEM CLASS ###



class Item:
	def __init__(self, name, recipe, rarity):
		self.name = name
		self.recipe = recipe
		self.rarity = rarity
		if name [-1] in ["s","x","z"] or name [-2:] in ["ss","sh","ch"]:
			  self.plural = name + "es"
		elif name [-1] == "y": self.plural = name [:-1] + "ies"
		else: self.plural = name + "s"



### ITEM TYPES ###



class Resource(Item):


	def __init__(self, type, rarity):
		
		self.recipe = None

		Item.__init__(*args, **kwargs)



class Weapon(Item):


	def __init__(self, type, recipe, rarity, speed, accuracy, damage, range, condition):
		
		self.recipe = recipe
		self.rarity = rarity
		self.speed = speed
		self.accuracy = accuracy
		self.damage = damage
		self.range = range
		self.condition = condition

		Item.__init__(*args, **kwargs)



class Projectile(Item):


	def __init__(self, type, recipe, rarity, speed, accuracy, damage, range):
		
		self.condition = None

		Item.__init__(*args, **kwargs)



class Launcher(Weapon):
	
	def __init__(self, type, recipe, rarity, speed, accuracy, range, has_scope, condition)
		
		self.has_scope = has_scope
		self.damage = None
		
		Weapon.__init__(*args, **kwargs)



### RESOURCES ###



class SoilPile(Resource):


	def __init__(self):
		
		self.type = "Soil Pile"
		self.rarity = "Common"

		Resource.__init__(type, rarity, *args, **kwargs)



class WoodChunk(Resource):


	def __init__(self):
		
		self.type = "Wood Chunk"
		self.rarity = "Common"

		Resource.__init__(type, rarity, *args, **kwargs)



class Vine(Resource):


	def __init__(self):
		
		self.type = "Vine"
		self.rarity = "Common"

		Resource.__init__(type, rarity, *args, **kwargs)



class Fruit(Resource):


	def __init__(self):
		
		self.type = "Fruit"
		self.rarity = "Common"

		Resource.__init__(type, rarity, *args, **kwargs)



class Rock(Resource):


	def __init__(self):
		
		self.type = "Rock"
		self.rarity = "Common"

		Resource.__init__(type, rarity, *args, **kwargs)



class WaterSupply(Resource):


	def __init__(self):
		
		self.type = "Water Supply"
		self.rarity = "Common"

		Resource.__init__(type, rarity, *args, **kwargs)



class SandPile(Resource):


	def __init__(self):
		
		self.type = "Sand Pile"
		self.rarity = "Common"

		Resource.__init__(type, rarity, *args, **kwargs)



class CactiChunk(Resource):


	def __init__(self):
		
		self.type = "Cacti Chunk"
		self.rarity = "Common"

		Resource.__init__(type, rarity, *args, **kwargs)



class IronChunk(Resource):


	def __init__(self):
		
		self.type = "Iron Chunk"
		self.rarity = "Uncommon"

		Resource.__init__(type, rarity, *args, **kwargs)



class Bone(Resource):


	def __init__(self):
		
		self.type = "Bone"
		self.rarity = "Common"

		Resource.__init__(type, rarity, *args, **kwargs)



class Diamond(Resource):


	def __init__(self):
		
		self.type = "Diamond"
		self.rarity = "Uncommon"

		Resource.__init__(type, rarity, *args, **kwargs)



class StoneChunk(Resource):


	def __init__(self):
		
		self.type = "Stone Chunk"
		self.rarity = "Common"

		Resource.__init__(type, rarity, *args, **kwargs)



class GoldNugget(Resource):


	def __init__(self):
		
		self.type = "Gold Nugget"
		self.rarity = "Uncommon"

		Resource.__init__(type, rarity, *args, **kwargs)



class Emerald(Resource):


	def __init__(self):
		
		self.type = "Emerald"
		self.rarity = "Uncommon"

		Resource.__init__(type, rarity, *args, **kwargs)



class QuartzShard(Resource):


	def __init__(self):
		
		self.type = "Quartz Shard"
		self.rarity = "Uncommon"

		Resource.__init__(type, rarity, *args, **kwargs)



class Explosive(Resource):


	def __init__(self):
		
		self.type = "Explosive"
		self.rarity = "Common"

		Resource.__init__(type, rarity, *args, **kwargs)



### ITEMS ###



class HarvestersArmor(Item):


		def __init__(self):

			self.type = "Harvester's Armor"
			self.rarity = "Rare"
			self.recipe = None

			Item.__init__(type, recipe, rarity, *args, **kwargs)



class Protector(Item):


		def __init__(self):

			self.type = "Protector"
			self.rarity = "Legendary"
			self.recipe = None

			Item.__init__(type, recipe, rarity, *args, **kwargs)



class Strawman(Item):


		def __init__(self):

			self.type = "Strawman"
			self.rarity = "Rare"
			self.recipe = None

			Item.__init__(type, recipe, rarity, *args, **kwargs)



class Coffin(Item):


		def __init__(self):

			self.type = "Coffin"
			self.rarity = "Legendary"
			self.recipe = None

			Item.__init__(type, recipe, rarity, *args, **kwargs)



class Ladder(Item):


		def __init__(self):

			self.type = "Ladder"
			self.rarity = "Rare"
			self.recipe = None

			Item.__init__(type, recipe, rarity, *args, **kwargs)



class MobRepellent(Item):


		def __init__(self):

			self.type = "Mob Repellent"
			self.rarity = "Legendary"
			self.recipe = None

			Item.__init__(type, recipe, rarity, *args, **kwargs)



class BottledWave(Item):


		def __init__(self):

			self.type = "Bottled Wave"
			self.rarity = "Rare"
			self.recipe = None

			Item.__init__(type, recipe, rarity, *args, **kwargs)



class BottledWind(Item):


		def __init__(self):

			self.type = "Bottled Wind"
			self.rarity = "Legendary"
			self.recipe = None

			Item.__init__(type, recipe, rarity, *args, **kwargs)



class Glider(Item):


		def __init__(self):

			self.type = "Harvester's Armor"
			self.rarity = "Rare"
			self.recipe = None

			Item.__init__(type, recipe, rarity, *args, **kwargs)



class Binoculars(Item):


		def __init__(self):

			self.type = "Binoculars"
			self.rarity = "Legendary"
			self.recipe = None

			Item.__init__(type, recipe, rarity, *args, **kwargs)



### WEAPONS ###



class Arm(Launcher):


	def __init__(self, condition):

		self.type = "Arm"
		self.recipe = None
		self.rarity = None
		self.speed = 1
		self.accuracy = 0.9
		self.range = 2
		self.has_scope = False
		
		Launcher.__init__(type, recipe, rarity, speed, accuracy, range, has_scope, *args, **kwargs)



class Bow(Launcher):


	def __init__(self, condition):

		self.type = "Bow"
		self.recipe = {Wood: 8, Vine: 1}
		self.rarity = "Common"
		self.speed = 1.25
		self.accuracy = 0.6
		self.range = 3
		self.has_scope = False
		
		Launcher.__init__(type, recipe, rarity, speed, accuracy, range, has_scope, *args, **kwargs)



class Crossbow(Launcher):


	def __init__(self, condition):

		self.type = "Crossbow"
		self.recipe = {Wood: 10, Vine: 2}
		self.rarity = "Common"
		self.speed = 1.25
		self.accuracy = 60
		self.range = 3
		self.has_scope = True
		
		Launcher.__init__(type, recipe, rarity, speed, accuracy, range, has_scope, *args, **kwargs)



class CombatBucket(Launcher):


	def __init__(self, condition):

		self.type = "Combat Bucket"
		self.recipe = {Iron: 12}
		self.rarity = "Common"
		self.speed = 1.75
		self.accuracy = 1
		self.range = 0
		self.has_scope = False
		
		Launcher.__init__(type, recipe, rarity, speed, accuracy, range, has_scope, *args, **kwargs)



class Slingshot(Launcher):


	def __init__(self, condition):

		self.type = "Slingshot"
		self.recipe = {Wood: 8, Vine: 1}
		self.rarity = "Common"
		self.speed = 0.75
		self.accuracy = 0.9
		self.range = 1
		self.has_scope = False
		
		Launcher.__init__(type, recipe, rarity, speed, accuracy, range, has_scope, *args, **kwargs)



class Cannon(Launcher):


	def __init__(self, condition):

		self.type = "Cannon"
		self.recipe = {Iron: 2, Wood: 200, Explosive: 2}
		self.rarity = "Uncommon"
		self.speed = 10
		self.accuracy = 1
		self.range = 1
		self.has_scope = False
		
		Launcher.__init__(type, recipe, rarity, speed, accuracy, range, has_scope, *args, **kwargs)



class RocketLauncher(Launcher):


	def __init__(self, condition):

		self.type = "Rocket Launcher"
		self.recipe = {Iron: 20, Stone: 200, Explosive: 6}
		self.rarity = "Rare"
		self.speed = 25
		self.accuracy = 1
		self.range = 6
		self.has_scope = True
		
		Launcher.__init__(type, recipe, rarity, speed, accuracy, range, has_scope, *args, **kwargs)



class MissileLauncher(Launcher):


	def __init__(self, condition):

		self.type = "Missile Launcher"
		self.recipe = {Iron: 50, Stone: 200, Wood: 50, Explosive: 8}
		self.rarity = "Legendary"
		self.speed = 40
		self.accuracy = 1
		self.range = 8
		self.has_scope = True
		
		Launcher.__init__(type, recipe, rarity, speed, accuracy, range, has_scope, *args, **kwargs)



class Fists(Weapon):


	def __init__(self, condition):

		self.type = "Fists"
		self.recipe = None
		self.rarity = None
		self.speed = 0.5
		self.accuracy = 1
		self.damage = 5
		self.range = 0
		
		Weapon.__init__(type, recipe, rarity, speed, accuracy, damage, range, *args, **kwargs)



class BoneBlade(Weapon):


	def __init__(self, condition):

		self.type = "Bone Blade"
		self.recipe = {Bone: 3}
		self.rarity = "Common"
		self.speed = 1.25
		self.accuracy = 0.9
		self.damage = 10
		self.range = 0
		
		Weapon.__init__(type, recipe, rarity, speed, accuracy, damage, range, *args, **kwargs)



class BoneStriker(Weapon):


	def __init__(self, condition):

		self.type = "Bone Striker"
		self.recipe = {Bone: 8}
		self.rarity = "Uncommon"
		self.speed = 1.25
		self.accuracy = 0.9
		self.damage = 25
		self.range = 0
		
		Weapon.__init__(type, recipe, rarity, speed, accuracy, damage, range, *args, **kwargs)



class WoodenSword(Weapon):


	def __init__(self, condition):

		self.type = "Wooden Sword"
		self.recipe = {Wood: 8}
		self.rarity = "Common"
		self.speed = 1
		self.accuracy = 0.8
		self.damage = 17
		self.range = 0
		
		Weapon.__init__(type, recipe, rarity, speed, accuracy, damage, range, *args, **kwargs)