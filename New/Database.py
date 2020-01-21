"""
Database.py
NewScript
Contains all the data for the game
"""


from colorama import Fore , Back , init , Style
from time import time


### CONSTANTS ###


EnvCleanupFactor = 50
EnvInconsistency = 1.01
EnvClusterSize = 5
CollectDelay = 60
MoveDelay = 0 #### 5
HarvestSize = 4
UncommonResourceThreshold = 75
RareResourceThreshold = 16
PrintSeparater = "print ('-----------------------------------------------')"


### LISTS ###


Environments = ["Woodlands" , "Plains" , "Grasslands" , "Waterlands" , "Rockylands"]
BiomeWeights = [60 , 20 , 5 , 1]
ResourceWeights = [40 , 40 , 16 , 4]


### DICTS ###


Commands = {
    "help" : "View the command list",
    "exit" : "Exit the program",
    "start" : "Start the game",
    "controls" : "View the controls"
    }
KeyBindings = {
    b"w" : ("Player .turn ('North')" , "Turn to the north"),
    b"s" : ("Player .turn ('South')" , "Turn to the south"),
    b"a" : ("Player .turn ('West')" , "Turn to the west"),
    b"d" : ("Player .turn ('East')" , "Turn to the east"),
    b" " : ("Player .move ()" , "Move forward"),
    b"j" : ("Player .collect ()" , "Collect resources"),
    b"k" : ("Player .attack ()" , "Attack with current weapon"),
    b"q" : ("Player .describe_surroundings ()" , "Give detailed location information"),
    b"e" : ("Player .look ()" , "Reveal the square ahead"),
    b"h" : ("Player .list_inv ()" , "View your inventory"),
    b"`" : ("command_input ()" , "Exit to the main menu")
    }
PrintColors = {
    "Critical" : Fore.RED,
    "Urgent" : Fore.YELLOW,
    "Rare" : Fore.CYAN,
    "Uncommon" : Fore.GREEN,
    "Common" : "",
    "Reset" : Style.RESET_ALL,
    }
