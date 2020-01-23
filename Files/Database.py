"""
Database.py
NewScript
Contains all the data for the game
"""


from colorama import Fore, Back, init, Style


### CONSTANTS ###


ENV_CLEANUP_FACTOR = 50
ENV_INCONSISTENCY = 1.01
ENV_CLUSTER_SIZE = 5
COLLECT_DELAY = 60
MOVE_DELAY = 0 #### 5
HARVEST_SIZE = 4
UNCOMMON_RESOURCE_THRESHOLD = 75
RARE_RESOURCE_THRESHOLD = 16
PRINT_SEPARATER = "print('-----------------------------------------------')"


### LISTS ###


ENVIRONMENTS = ["Woodlands", "Plains", "Grasslands", "Waterlands", "Rockylands"]
BIOME_WEIGHTS = [60, 20, 5, 1]
RESOURCE_WEIGHTS = [40, 40, 16, 4]


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
	b" ": ("self.Player.move(self)", "Move forward"),
	b"j": ("self.Player.collect()", "Collect resources"),
	b"k": ("self.Player.attack()", "Attack with current weapon"),
	b"q": ("self.Player.describe_surroundings()", "Give detailed location information"),
	b"e": ("self.Player.look(self)", "Reveal the square ahead"),
	b"h": ("self.Player.list_inv()", "View your inventory"),
	b"`": ("self.command_input()", "Pause game")
	}
PRINT_COLORS = {
	"Critical": Fore.RED,
	"Urgent": Fore.YELLOW,
	"Rare": Fore.CYAN,
	"Uncommon": Fore.GREEN,
	"Common": "",
	"Reset": Style.RESET_ALL,
	}
