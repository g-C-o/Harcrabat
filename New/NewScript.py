"""
NewScript Version 0.5
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
import msvcrt


### START CODE ###


class Game:

    
    def __init__(self):
        
        ## Player:    
        self.Player = Character("Player 1", 0, [], [], [[time() - CollectDelay for Square in range(50)] for Row in range(50)], 100, 100, {}, None, None, [26,26], "North", time())

        ## Resources:
        #### Plurals: Change to plural algorithm.
        ####    Pass in Plural Type and have class
        ####    produce actual plural
        ####   ... One single Plural type calculates -s vs -es?
        ####    or separate types?
        Bark = Resource("Bark Strip", 4, "Bark Strips")
        Soil = Resource("Soil Pile", 360, "Soil Piles")
        Wood = Resource("Wood Block", 252, "Wood Blocks")
        Leaves = Resource("Leaf Pile", 32, "Leaf Piles")
        Vines = Resource("Vine", 16, "Vines")
        Moss = Resource("Moss Piece", 4, "Moss Pieces")
        Fruit = Resource("Fruit", 56, "Fruits")
        Rocks = Resource("Rock", 100, "Rocks")
        Gravel = Resource("Gravel Pile", 100, "Gravel Piles")
        Water = Resource("Water Supply", 180, "Water Supplies")
        Sand = Resource("Sand Pile", 160, "Sand Piles")
        Cacti = Resource("Cacti Block", 16, "Cacti Blocks")
        Iron = Resource("Iron Nugget", 124, "Iron Nuggets")
        Snow = Resource("Snow Pile", 80, "Snow Piles")
        Bones = Resource("Bone", 16, "Bones")
        Diamonds = Resource("Diamond", 8, "Diamonds")
        Stone = Resource("Stone", 216, "Stone Blocks")
        Flowers = Resource("Flower Bundle", 40, "Flower Bundles")
        Clay = Resource("Clay Pile", 32, "Clay Piles")
        Gold = Resource("Gold Nugget", 40, "Gold Nuggets")
        Mud = Resource("Mud Pile", 40, "Mud Piles")
        Emeralds = Resource("Emerald", 8, "Emeralds")
        Quartz = Resource("Quartz Shard", 20, "Quartz Shards")

        ## Items:
        HarvesterArmor = Item(None)
        Protector = Item(None)
        Strawman = Item(None)
        Coffin = Item(None)
        Ladder = Item(None)
        MobRepellant = Item(None)
        BottledWave = Item(None)
        BottledWind = Item(None)
        Gliders = Item(None)
        Binoculars = Item(None)

        ## Mobs:
        Fighter = Mob()
        Predator = Mob()
        Goblin = Mob()
        Destroyer = Mob()
        Annihilator = Mob()
        Troll = Mob()
        Raider = Mob()
        Minion = Mob()
        Zombie = Mob()
        Defender = Mob()
        Guardian = Mob()
        Skeleton = Mob()
        Hunter = Mob()
        Assasin = Mob()
        Ghoul = Mob()

        ## Animals:
        Chicken = Animal()
        Rabbit = Animal()
        Cow = Animal()
        Fish = Animal()
        Sheep = Animal()

        ## Biomes:
        Forest = Biome("Forest", "into a", Soil, Wood, Leaves, Bark, Fighter, Fighter, Fighter, Chicken, None, None)
        Jungle = Biome("Jungle", "into a", Soil, Wood, Vines, Moss, Fighter, Fighter, Predator, Chicken, None, None)
        Grove = Biome("Grove", "into a", Soil, Wood, Fruit, Rocks, Fighter, Predator, Fighter, Chicken, None, None)
        Garden = Biome("Garden", "into a", Soil, Fruit, Gravel, Water, Fighter, Predator, Goblin, Chicken, HarvesterArmor, Protector)
        Desert = Biome("Desert", "into a", Sand, Rocks, Cacti, Iron, Destroyer, Destroyer, Destroyer, Rabbit, None, None)
        Tundra = Biome("Tundra", "into a", Snow, Rocks, Iron, Wood, Destroyer, Destroyer, Annihilator, Rabbit, None, None)
        Badland = Biome("Badland", "into a", Sand, Snow, Bones, Diamonds, Destroyer, Annihilator, Destroyer, Rabbit, None, None)
        Temple = Biome("Temple", "into a", Sand, Iron, Wood, Gold, Destroyer, Annihilator, Troll, Rabbit, Strawman, Coffin)
        Prairie = Biome("Prairie", "into a", Soil, Gravel, Stone, Iron, Raider, Raider, Raider, Cow, None, None)
        Meadow = Biome("Meadow", "into a", Soil, Flowers, Clay, Gold, Raider, Raider, Minion, Cow, None, None)
        Swamp = Biome("Swamp", "into a", Mud, Water, Gold, Iron, Raider, Minion, Raider, Cow, None, None)
        Fort = Biome("Fort", "into a", Wood, Stone, Iron, Diamonds, Raider, Minion, Zombie, Cow, Ladder, MobRepellant)
        Lake = Biome("Lake", "into a", Water, Soil, Rocks, Emeralds, Defender, Defender, Defender, Fish, None, None)
        Beach = Biome("Beach", "into a", Water, Sand, Clay, Emeralds, Defender, Defender, Guardian, Fish, None, None)
        Island = Biome("Island", "onto an", Soil, Iron, Water, Quartz, Defender, Guardian, Defender, Fish, None, None)
        Shipwreck = Biome("Shipwreck", "into a", Wood, Water, Gold, Quartz, Defender, Guardian, Skeleton, Fish, BottledWave, BottledWind)
        Mountain = Biome("Mountain", "onto a", Stone, Soil, Wood, Quartz, Hunter, Hunter, Hunter, Sheep, None, None)
        Canyon = Biome("Canyon", "into a", Stone, Gravel, Leaves, Quartz, Hunter, Hunter, Assasin, Sheep, None, None)
        Cave = Biome("Cave", "into a", Stone, Iron, Wood, Quartz, Hunter, Assasin, Hunter, Sheep, None, None)
        Monument = Biome("Monument", "into a", Iron, Stone, Diamonds, Gravel, Hunter, Assasin, Ghoul, Sheep, Gliders, Binoculars)

        ## Environments:
        Woodlands = Environment(Forest, Jungle, Grove, Garden)
        Plains = Environment(Desert, Tundra, Badland, Temple)
        Grasslands = Environment(Prairie, Meadow, Swamp, Fort)
        Waterlands = Environment(Lake, Beach, Island, Shipwreck)
        Rockylands = Environment(Mountain, Canyon, Cave, Monument)

        self.startup()


    ### GAME FUNCTIONS ###
    

    def create_player(self):
        desired_name = input("Enter your name:\n| ")
        eval(PrintSeparater)
        self.Player.set_name(desired_name)

    
    def load_map(self):
        print("Loading Map")

        ## Preload Map:
        print("\tCreating Seed")
        Map = [[None 
                if ColIndex in [0,51]
                or RowIndex in [0,51]
                else choices(("Woodlands", "Plains", "Grasslands", "Waterlands", "Rockylands"))[0]
            for ColIndex in range(52)]
            for RowIndex in range(52)]
        
        ## Choose Environments:
        print("\tGenerating Chunks")
        for Rep in range(EnvCleanupFactor):
            Map = [[None
                    if ColIndex in [0,51]
                    or RowIndex in [0,51]
                    else Environment.choose([Map[RowIndex-1][ColIndex-1], Map[RowIndex-1][ColIndex], Map[RowIndex-1][ColIndex+1], Map[RowIndex][ColIndex-1], Map[RowIndex][ColIndex+1], Map[RowIndex+1][ColIndex-1], Map[RowIndex+1][ColIndex], Map[RowIndex+1][ColIndex+1]])
                for ColIndex in range(len(Map[RowIndex]))]
                for RowIndex in range(len(Map))]
        Map = [[Env for Env in Row[1:-1]] for Row in Map[1:-1]]

        ## Choose Biomes:
        print("\tGenerating Terrain")
        BiomeMap = [[Biome.choose(Env)
            for Env in Row]
            for Row in Map]
        
        Player.Map = Map
        Player.BiomeMap = BiomeMap

        return Map, BiomeMap


    def run_game(self):
        ## Wait for keypress:
        while True:
            while not msvcrt.kbhit():
                pass
                #### Update game
            KeyInput = msvcrt.getch()
            
            ## Respond to keypress:
            if KeyInput in KeyBindings:
                eval(KeyBindings[KeyInput][0])


    def update_game(self):
        #### Update health and energy
        #### Regenerate resources in exhausted squares
        #### Spawn stuff
        pass


    ### COMMAND FUNCTIONS ###


    def help(self):
        [print(Command+ ": " + Commands[Command]) for Command in Commands]


    def start(self):
        self.create_player()
        Map, BiomeMap = self.load_map()
        eval(PrintSeparater)
        Player.describe_spawnpoint()
        run_game()


    def controls(self):
        for Key in KeyBindings:
            if Key == b" ": Letter = "SPACE"
            else: Letter = Key.decode("utf-8")
            print(Letter + ": " + KeyBindings[Key][1])        


    ### MANAGER FUNCTIONS ###


    def command_input(self):
        eval(PrintSeparater)
        Command = (input("| ")).lower()
        eval(PrintSeparater)
        if Command in Commands : eval("self." + Command + "()")
        else : print("Invalid Command")

        
    def startup(self):
        init()
        print("NewScript version 0.5")
        print("Type 'help' for the command list.")
        while True:
            self.command_input()
        
    
if __name__ == "__main__": Game()
