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


	def __init__(self, type, recipe, rarity, damage):
		
		self.condition = None

		Item.__init__(condition, *args, **kwargs)



class Launcher(Weapon):
	
	def __init__(self, type, recipe, rarity, speed, accuracy, range, has_scope, condition):
		
		self.has_scope = has_scope
		self.damage = None
		
		Weapon.__init__(damage, *args, **kwargs)



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
		self.rarity = "Common"
		self.speed = 5
		self.accuracy = 1
		self.range = 1
		self.has_scope = False
		
		Launcher.__init__(type, recipe, rarity, speed, accuracy, range, has_scope, *args, **kwargs)



class RocketLauncher(Launcher):


	def __init__(self, condition):

		self.type = "Rocket Launcher"
		self.recipe = {Iron: 20, Stone: 100, Wood: 100, Explosive: 6}
		self.rarity = "Uncommon"
		self.speed = 10
		self.accuracy = 1
		self.range = 6
		self.has_scope = True
		
		Launcher.__init__(type, recipe, rarity, speed, accuracy, range, has_scope, *args, **kwargs)



class MissileLauncher(Launcher):


	def __init__(self, condition):

		self.type = "Missile Launcher"
		self.recipe = {Iron: 50, Stone: 200, Wood: 50, Explosive: 8}
		self.rarity = "Rare"
		self.speed = 12
		self.accuracy = 1
		self.range = 8
		self.has_scope = True
		
		Launcher.__init__(type, recipe, rarity, speed, accuracy, range, has_scope, *args, **kwargs)



class NukeLauncher(Launcher):


	def __init__(self, condition):

		self.type = "Nuke Launcher"
		self.recipe = {Iron: 100, Stone: 300, Wood: 100, Explosive: 15}
		self.rarity = "Legendary"
		self.speed = 15
		self.accuracy = 1
		self.range = 15
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



class StoneSword(Weapon):


	def __init__(self, condition):

		self.type = "Stone Sword"
		self.recipe = {Stone: 10, Wood: 3}
		self.rarity = "Common"
		self.speed = 1
		self.accuracy = 0.8
		self.damage = 20
		self.range = 0
		
		Weapon.__init__(type, recipe, rarity, speed, accuracy, damage, range, *args, **kwargs)



class IronSword(Weapon):


	def __init__(self, condition):

		self.type = "Iron Sword"
		self.recipe = {Iron: 10, Wood: 3}
		self.rarity = "Uncommon"
		self.speed = 1
		self.accuracy = 0.8
		self.damage = 23
		self.range = 0
		
		Weapon.__init__(type, recipe, rarity, speed, accuracy, damage, range, *args, **kwargs)



class DiamondSword(Weapon):


	def __init__(self, condition):

		self.type = "Diamond Sword"
		self.recipe = {Diamond: 10, Wood: 3}
		self.rarity = "Rare"
		self.speed = 1
		self.accuracy = 0.8
		self.damage = 26
		self.range = 0
		
		Weapon.__init__(type, recipe, rarity, speed, accuracy, damage, range, *args, **kwargs)



class WoodenAxe(Weapon):


	def __init__(self, condition):

		self.type = "Wooden Axe"
		self.recipe = {Wood: 9}
		self.rarity = "Common"
		self.speed = 1.5
		self.accuracy = 0.7
		self.damage = 26
		self.range = 0
		
		Weapon.__init__(type, recipe, rarity, speed, accuracy, damage, range, *args, **kwargs)



class StoneAxe(Weapon):


	def __init__(self, condition):

		self.type = "Stone Axe"
		self.recipe = {Stone: 10, Wood: 4}
		self.rarity = "Common"
		self.speed = 1.5
		self.accuracy = 0.7
		self.damage = 30
		self.range = 0
		
		Weapon.__init__(type, recipe, rarity, speed, accuracy, damage, range, *args, **kwargs)



class IronAxe(Weapon):


	def __init__(self, condition):

		self.type = "Iron Axe"
		self.recipe = {Iron: 10, Wood: 4}
		self.rarity = "Uncommon"
		self.speed = 1.5
		self.accuracy = 0.7
		self.damage = 34
		self.range = 0
		
		Weapon.__init__(type, recipe, rarity, speed, accuracy, damage, range, *args, **kwargs)



class DiamondAxe(Weapon):


	def __init__(self, condition):

		self.type = "Diamond Axe"
		self.recipe = {Diamond: 10, Wood: 4}
		self.rarity = "Rare"
		self.speed = 1.5
		self.accuracy = 0.7
		self.damage = 38
		self.range = 0
		
		Weapon.__init__(type, recipe, rarity, speed, accuracy, damage, range, *args, **kwargs)



class WoodenSpear(Weapon):


	def __init__(self, condition):

		self.type = "Wooden Spear"
		self.recipe = {Wood: 10}
		self.rarity = "Common"
		self.speed = 1.75
		self.accuracy = 0.6
		self.damage = 30
		self.range = 1
		
		Weapon.__init__(type, recipe, rarity, speed, accuracy, damage, range, *args, **kwargs)



class StoneSpear(Weapon):


	def __init__(self, condition):

		self.type = "Stone Spear"
		self.recipe = {Stone: 10, Wood: 5}
		self.rarity = "Common"
		self.speed = 1.75
		self.accuracy = 0.6
		self.damage = 35
		self.range = 1
		
		Weapon.__init__(type, recipe, rarity, speed, accuracy, damage, range, *args, **kwargs)



class IronSpear(Weapon):


	def __init__(self, condition):

		self.type = "Iron Spear"
		self.recipe = {Iron: 10, Wood: 5}
		self.rarity = "Uncommon"
		self.speed = 1.75
		self.accuracy = 0.6
		self.damage = 40
		self.range = 1
		
		Weapon.__init__(type, recipe, rarity, speed, accuracy, damage, range, *args, **kwargs)



class DiamondSpear(Weapon):


	def __init__(self, condition):

		self.type = "Diamond Spear"
		self.recipe = {Diamond: 10, Wood: 5}
		self.rarity = "Rare"
		self.speed = 1.75
		self.accuracy = 0.6
		self.damage = 45
		self.range = 1
		
		Weapon.__init__(type, recipe, rarity, speed, accuracy, damage, range, *args, **kwargs)



class WoodenBoomerang(Weapon):


	def __init__(self, condition):

		self.type = "Wooden Boomerang"
		self.recipe = {Wood: 12}
		self.rarity = "Common"
		self.speed = 3
		self.accuracy = 0.9
		self.damage = 40
		self.range = 2
		
		Weapon.__init__(type, recipe, rarity, speed, accuracy, damage, range, *args, **kwargs)



class StoneBoomerang(Weapon):


	def __init__(self, condition):

		self.type = "Stone Boomerang"
		self.recipe = {Stone: 10, Wood: 6}
		self.rarity = "Common"
		self.speed = 3
		self.accuracy = 0.9
		self.damage = 50
		self.range = 2
		
		Weapon.__init__(type, recipe, rarity, speed, accuracy, damage, range, *args, **kwargs)



class IronBoomerang(Weapon):


	def __init__(self, condition):

		self.type = "Iron Boomerang"
		self.recipe = {Iron: 10, Wood: 6}
		self.rarity = "Uncommon"
		self.speed = 3
		self.accuracy = 0.9
		self.damage = 60
		self.range = 2
		
		Weapon.__init__(type, recipe, rarity, speed, accuracy, damage, range, *args, **kwargs)



class DiamondBoomerang(Weapon):


	def __init__(self, condition):

		self.type = "Iron Sword"
		self.recipe = {Diamond: 10, Wood: 6}
		self.rarity = "Rare"
		self.speed = 3
		self.accuracy = 0.9
		self.damage = 70
		self.range = 2
		
		Weapon.__init__(type, recipe, rarity, speed, accuracy, damage, range, *args, **kwargs)



class Bomb(Weapon):


	def __init__(self, condition):

		self.type = "Bomb"
		self.recipe = {Stone: 25, Wood: 25, Explosive: 5}
		self.rarity = "Common"
		self.speed = 15
		self.accuracy = 1
		self.damage = 100
		self.range = 0
		
		Weapon.__init__(type, recipe, rarity, speed, accuracy, damage, range, *args, **kwargs)



class Grenade(Weapon):


	def __init__(self, condition):

		self.type = "Grenade"
		self.recipe = {Stone: 4, Wood: 4, Explosive: 2}
		self.rarity = "Common"
		self.speed = 1
		self.accuracy = 1
		self.damage = 65
		self.range = 0
		
		Weapon.__init__(type, recipe, rarity, speed, accuracy, damage, range, *args, **kwargs)



class Dynamite(Weapon):


	def __init__(self, condition):

		self.type = "Dynamite"
		self.recipe = {Explosive: 1}
		self.rarity = "Common"
		self.speed = 1
		self.accuracy = 1
		self.damage = 40
		self.range = 0
		
		Weapon.__init__(type, recipe, rarity, speed, accuracy, damage, range, *args, **kwargs)



### WEAPONS ###



#### Ball: Lost on kill
#### Arrow: Lost on hit
#### Clump: Lost always
#### Spike: Lost on hit
#### Cn, Rk, Ms: Lost always
class WoodenBall(Projectile):


	def __init__(self):

		self.type = "Wooden ball"
		self.recipe = {Wood: 5}
		self.rarity = "Common"
		self.damage = 15

		Projectile.__init__(type, recipe, rarity, damage, *args, **kwargs)



class StoneBall(Projectile):


	def __init__(self):

		self.type = "Stone ball"
		self.recipe = {Wood: 5, Stone: 2}
		self.rarity = "Common"
		self.damage = 18

		Projectile.__init__(type, recipe, rarity, damage, *args, **kwargs)



class IronBall(Projectile):


	def __init__(self):

		self.type = "Iron ball"
		self.recipe = {Wood: 5, Iron: 2}
		self.rarity = "Common"
		self.damage = 21

		Projectile.__init__(type, recipe, rarity, damage, *args, **kwargs)



class DiamondBall(Projectile):


	def __init__(self):

		self.type = "Diamond ball"
		self.recipe = {Wood: 5, Diamond: 2}
		self.rarity = "Uncommon"
		self.damage = 24

		Projectile.__init__(type, recipe, rarity, damage, *args, **kwargs)



class WoodenArrow(Projectile):


	def __init__(self):

		self.type = "Wooden Arrow"
		self.recipe = {Wood: 3}
		self.rarity = "Common"
		self.damage = 17

		Projectile.__init__(type, recipe, rarity, damage, *args, **kwargs)



class StoneArrow(Projectile):


	def __init__(self):

		self.type = "Stone Arrow"
		self.recipe = {Wood: 3, Stone: 2}
		self.rarity = "Common"
		self.damage = 20

		Projectile.__init__(type, recipe, rarity, damage, *args, **kwargs)



class IronArrow(Projectile):


	def __init__(self):

		self.type = "Iron Arrow"
		self.recipe = {Wood: 3, Iron: 3}
		self.rarity = "Common"
		self.damage = 23

		Projectile.__init__(type, recipe, rarity, damage, *args, **kwargs)



class DiamondArrow(Projectile):


	def __init__(self):

		self.type = "Diamond Arrow"
		self.recipe = {Wood: 3, Diamond: 1}
		self.rarity = "Uncommon"
		self.damage = 26

		Projectile.__init__(type, recipe, rarity, damage, *args, **kwargs)



class SoilClump(Projectile):


	def __init__(self):

		self.type = "Soil Clump"
		self.recipe = {Soil: 4}
		self.rarity = "Common"
		self.damage = 38

		Projectile.__init__(type, recipe, rarity, damage, *args, **kwargs)



class SandClump(Projectile):


	def __init__(self):

		self.type = "Sand Clump"
		self.recipe = {Sand: 4}
		self.rarity = "Common"
		self.damage = 38

		Projectile.__init__(type, recipe, rarity, damage, *args, **kwargs)



class CactusClump(Projectile):


	def __init__(self):

		self.type = "Cactus Clump"
		self.recipe = {Cactus: 3}
		self.rarity = "Common"
		self.damage = 55

		Projectile.__init__(type, recipe, rarity, damage, *args, **kwargs)



class WoodenSpike(Projectile):


	def __init__(self):

		self.type = "Wooden Spike"
		self.recipe = {Wood: 2}
		self.rarity = "Common"
		self.damage = 17

		Projectile.__init__(type, recipe, rarity, damage, *args, **kwargs)



class StoneSpike(Projectile):


	def __init__(self):

		self.type = "Stone Spike"
		self.recipe = {Stone: 3}
		self.rarity = "Common"
		self.damage = 19

		Projectile.__init__(type, recipe, rarity, damage, *args, **kwargs)



class IronSpike(Projectile):


	def __init__(self):

		self.type = "Iron Spike"
		self.recipe = {Iron: 1, Wood: 2}
		self.rarity = "Common"
		self.damage = 21

		Projectile.__init__(type, recipe, rarity, damage, *args, **kwargs)



class DiamondSpike(Projectile):


	def __init__(self):

		self.type = "Diamond Spike"
		self.recipe = {Diamond: 1, Wood: 2}
		self.rarity = "Uncommon"
		self.damage = 26

		Projectile.__init__(type, recipe, rarity, damage, *args, **kwargs)



class CannonBall(Projectile):


	def __init__(self):

		self.type = "Cannon Ball"
		self.recipe = {Wood: 10, Stone: 15, Explosive: 2}
		self.rarity = "Common"
		self.damage = 125

		Projectile.__init__(type, recipe, rarity, damage, *args, **kwargs)



class Rocket(Projectile):


	def __init__(self):

		self.type = "Rocket"
		self.recipe = {Iron: 10, Explosive: 5}
		self.rarity = "Uncommon"
		self.damage = 150

		Projectile.__init__(type, recipe, rarity, damage, *args, **kwargs)



class Missile(Projectile):


	def __init__(self):

		self.type = "Missile"
		self.recipe = {Iron: 15, Explosive: 10}
		self.rarity = "Rare"
		self.damage = 200

		Projectile.__init__(type, recipe, rarity, damage, *args, **kwargs)



class Nuke(Projectile):


	def __init__(self):

		self.type = "Nuke"
		self.recipe = {Iron: 25, Explosive: 50}
		self.rarity = "Legendary"
		self.damage = 1000

		Projectile.__init__(type, recipe, rarity, damage, *args, **kwargs)
		