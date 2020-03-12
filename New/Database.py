"""
Database.py
Harcrabat
Contains all the data for the game
"""


from colorama import Fore, Back, init, Style


### VALUES ###


HARCRABAT_VERSION = 0.9
ENV_CLEANUP_FACTOR = 50
ENV_INCONSISTENCY = 1.01
ENV_CLUSTER_SIZE = 5
COLLECT_DELAY = 0 #### 60
MOVE_DELAY = 0 #### 5
MOB_REPLACE_DELAY = 0 #### 15
HARVEST_SIZE = 4
NUMBER_OF_MOBS = 200
MOB_BATCH_SIZE = 10
MOB_MOVE_BATCH_SIZE = 100 
UNCOMMON_RESOURCE_THRESHOLD = 75
RARE_RESOURCE_THRESHOLD = 16
ANIMAL_HEALTH = 50


### STRINGS ###


PRINT_SEPARATER = "print('-----------------------------------------------')"
STARTUP_MESSAGE = "Harcrabat version " + str(HARCRABAT_VERSION)


### LISTS ###


ITEM_NAMES = ["SoilPile", "WoodChunk", "Vine", "Fruit", "Rock", "WaterSupply", "SandPile", "CactiChunk", "IronChunk", "Bone", "Diamond", "StoneChunk", "GoldNugget", "Emerald", "QuartzShard", "Explosive", "HarvestersArmor", "Protector", "Strawman", "Coffin", "Ladder", "MobRepellent", "BottledWave", "BottledWind", "Glider", "Binoculars", "WoodenBall", "StoneBall", "IronBall", "DiamondBall", "WoodenArrow", "StoneArrow", "IronArrow", "DiamondArrow", "SoilClump", "SandClump", "CactusClump", "WoodenSpike", "StoneSpike", "IronSpike", "DiamondSpike", "CannonBall", "Rocket", "Missile", "Nuke", "Bow", "Crossbow", "Slingshot", "Cannon", "RocketLauncher", "MissileLauncher", "NukeLauncher", "BoneBlade", "BoneStriker", "WoodenSword", "StoneSword", "IronSword", "DiamondSword", "WoodenAxe", "StoneAxe", "IronAxe", "DiamondAxe", "WoodenSpear", "StoneSpear", "IronSpear", "DiamondSpear", "WoodenBoomerang", "StoneBoomerang", "IronBoomerang", "DiamondBoomerang", "Bomb", "Grenade", "Dynamite"]
ENVIRONMENT_NAMES = ["Woodlands", "Plains", "Grasslands", "Waterlands", "Rockylands"]
BIOME_WEIGHTS = [60, 20, 5, 1]
RESOURCE_WEIGHTS = [60, 35, 5]
MOB_TIER_WEIGHTS = [10, 20, 70]


### DICTS ###


COMMANDS = {
	"help": "View the command list",
	"exit": "Exit the program",
	"start": "Start the game",
	"controls": "View the controls"
	}
KEY_BINDINGS = {
	b"w": ("self.Player.turn('North')", "Turn to the north"),
	b"s": ("self.Player.turn('South')", "Turn to the south"),
	b"a": ("self.Player.turn('West')", "Turn to the west"),
	b"d": ("self.Player.turn('East')", "Turn to the east"),
	b" ": ("self.Player.move(self.mob_map)", "Move forward"),
	b"j": ("self.Player.collect()", "Collect resources"),
	b"k": ("self.Player.attack()", "Attack with current weapon"),
	b"q": ("self.Player.describe_surroundings()", "Give detailed location information"),
	b"e": ("self.Player.look()", "Reveal the square ahead"),
	b"h": ("self.Player.list_inv()", "View your inventory"),
	b"`": ("self.command_input()", "Pause game"),
	b"l": ("self.Player.craft()", "Craft an item")
	}
PRINT_COLORS = {
	"Critical": Fore.RED,
	"Legendary": Fore.BLUE,
	"Rare": Fore.CYAN,
	"Uncommon": Fore.GREEN,
	"Common": "",
	"Reset": Style.RESET_ALL,
	}
