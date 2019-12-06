""" Contains all the data for the game
"""

from random import choices
#from keyboard import add_hotkey
import getch

### CONSTANTS ###

## Dicts + Lists:
Commands = {
    "help" : "View the command list",
    "exit" : "Exit the program",
    "start" : "Start the game",
    }
Environments = ["Woodlands" , "Plains" , "Grasslands" , "Waterlands" , "Rockylands"]
BiomeWeights = [60,20,5,1]

## Values:
PrintSeparater = "print ('-----------------------------------------------')"
EnvCleanupFactor = 50
EnvInconsistency = 1.01
EnvClusterSize = 5

### DEFINE CLASSES ###

class Text:
    Red = '\033[31m'
    Green = '\033[32m'
    Blue = '\033[34m'
    White = '\033[37m'
    Black = '\033[30m'

class Environment:
    def __init__ (self , PrimaryBiome , SecondaryBiome , TertiaryBiome , AbandonedStructure):
        self .PriB = PrimaryBiome
        self .SecB = SecondaryBiome
        self .TerB = TertiaryBiome
        self .Structure = AbandonedStructure
    def choose (Surroundings):
        Surroundings = [Square for Square in Surroundings if Square] 
        EnvProbs = {Env : EnvInconsistency for Env in Environments}
        for Square in Surroundings:
            EnvProbs [Square] = EnvProbs [Square] * EnvClusterSize
        EnvWeights = [Prob for Prob in list (EnvProbs.values ())]
        EnvChoice = choices (Environments , weights=EnvWeights) [0]
        return EnvChoice

class Biome:
    def __init__ (self , Ground , PrimaryResource , SecondaryResource , TertiaryResource , PrimaryMob , SecondaryMob , TertiaryMob , Animal , PrimaryLoot , SecondaryLoot):
        self .GroundR = Ground
        self .PriR = PrimaryResource
        self .SecR = SecondaryResource
        self .TerR = TertiaryResource
        self .PriM = PrimaryMob
        self .SecM = SecondaryMob
        self .TerM = TertiaryMob
        self .Animal = Animal
        self .PriL = PrimaryLoot
        self .SecL = SecondaryLoot
    def choose (Env):
        EnvClass = eval(Env)
        BiomeChoice = choices ([EnvClass.PriB , EnvClass.SecB , EnvClass.TerB , EnvClass.Structure] , weights=BiomeWeights) [0]
        return BiomeChoice

class Animal:
    pass

class Item:
    pass

class Resource:
    pass

class Mob:
    pass

class Weapon:
    def __init__ (self , Recipe , WeaponType , Damage , Speed , Accuracy , Durability):
        self .Recipe = Recipe
        self .Type = WeaponType
        self .Damage = Damage
        self .Speed = Speed
        self .Accuracy = Accuracy

class Armor:
    def __init__ (self , Recipe , Protection , Durability):
        self .Recipe = Recipe
        self .Protection = Protection
        self .Durability = Durability

class Character:
    def __init__(self , Name , Score , Health , Energy , Inventory , HandItem , Armor , Location , Orientation):
        self .Name = Name
        self .Score = Score
        self .Health = Health
        self .Energy = Energy
        self .Inventory = Inventory
        self .HandItem = HandItem
        self .Armor = Armor
        self .Location = Location
        self .Orientation = Orientation

    def set_name (self, NewName):
        self .Name = NewName

    def switch_hand_item (self, NewItem):
        self .HandItem = NewItem

    def switch_armor (self, NewArmor):
        self .Armor = NewArmor
    
    def move (self):
        if self .Orientation  == "N":
            self .Location [0] -= 1
        elif self .Orientation  == "S":
            self .Location [0] += 1
        elif self .Orientation  == "W":
            self .Location [1] -= 1
        elif self .Orientation  == "E":
            self .Location [0] += 1
    
    def turn (self , NewOrientation):
        self .Orientation = NewOrientation

### CREATE INSTANCES ###

## Player:
Player = Character ("Player 1" , 0 , 100 , 100 , {} , None , None , [50,50] , "N")

## Resources:
Bark = Resource ()
Soil = Resource ()
Wood = Resource ()
Leaves = Resource ()
Vines = Resource ()
Moss = Resource ()
Fruit = Resource ()
Rocks = Resource ()
Gravel = Resource ()
Water = Resource ()
Sand = Resource ()
Cacti = Resource ()
Iron = Resource ()
Snow = Resource ()
Bones = Resource ()
Diamonds = Resource ()
Stone = Resource ()
Flowers = Resource ()
Clay = Resource ()
Gold = Resource ()
Mud = Resource ()
Emeralds = Resource ()
Quartz = Resource ()

## Items:
HarvesterArmor = Item ()
Protector = Item ()
Strawman = Item ()
Coffin = Item ()
Ladder = Item ()
MobRepellant = Item ()
BottledWave = Item ()
BottledWind = Item ()
Gliders = Item ()
Binoculars = Item ()

## Mobs:
Fighter = Mob ()
Predator = Mob ()
Goblin = Mob ()
Destroyer = Mob ()
Annihilator = Mob ()
Troll = Mob ()
Raider = Mob ()
Minion = Mob ()
Zombie = Mob ()
Defender = Mob ()
Guardian = Mob ()
Skeleton = Mob ()
Hunter = Mob ()
Assasin = Mob ()
Ghoul = Mob ()

## Animals:
Chicken = Animal ()
Rabbit = Animal ()
Cow = Animal ()
Fish = Animal ()
Sheep = Animal ()

## Biomes:
Forest = Biome (Soil , Wood , Leaves , Bark , Fighter , Fighter , Fighter , Chicken , None , None)
Jungle = Biome (Soil , Wood , Vines , Moss , Fighter , Fighter , Predator , Chicken , None , None)
Grove = Biome (Soil , Wood , Fruit , Rocks , Fighter , Predator , Fighter , Chicken , None , None)
Garden = Biome (Soil , Fruit , Gravel , Water , Fighter , Predator , Goblin , Chicken , HarvesterArmor , Protector)
Desert = Biome (Sand , Rocks , Cacti , Iron , Destroyer , Destroyer , Destroyer , Rabbit , None , None)
Tundra = Biome (Snow , Rocks , Iron , Wood , Destroyer , Destroyer , Annihilator , Rabbit , None , None)
Badlands = Biome (Sand , Snow , Bones , Diamonds , Destroyer , Annihilator , Destroyer , Rabbit , None , None)
Temple = Biome (Sand , Iron , Wood , Gold , Destroyer , Annihilator , Troll , Rabbit , Strawman , Coffin)
Prarie = Biome (Soil , Gravel , Stone , Iron , Raider , Raider , Raider , Cow , None , None)
Meadow = Biome (Soil , Flowers , Clay , Gold , Raider , Raider , Minion , Cow , None , None)
Swamp = Biome (Mud , Water , Gold , Iron , Raider , Minion , Raider , Cow , None , None)
Fort = Biome (Wood , Stone , Iron , Diamonds , Raider , Minion , Zombie , Cow , Ladder , MobRepellant)
Lake = Biome (Water , Soil , Rocks , Emeralds , Defender , Defender , Defender , Fish , None , None)
Beach = Biome (Water , Sand , Clay , Emeralds , Defender , Defender , Guardian , Fish , None , None)
Island = Biome (Soil , Iron , Water , Quartz , Defender , Guardian , Defender , Fish , None , None)
Shipwreck = Biome (Wood , Water , Gold , Quartz , Defender , Guardian , Skeleton , Fish , BottledWave , BottledWind)
Mountain = Biome (Stone , Soil , Wood , Quartz , Hunter , Hunter , Hunter , Sheep , None , None)
Canyon = Biome (Stone , Gravel , Leaves , Quartz , Hunter , Hunter , Assasin , Sheep , None , None)
Cave = Biome (Stone , Iron , Wood , Quartz , Hunter , Assasin , Hunter , Sheep , None , None)
Monument = Biome (Iron , Stone , Diamonds , Gravel , Hunter , Assasin , Ghoul , Sheep , Gliders , Binoculars)

## Environments:
Woodlands = Environment (Forest , Jungle , Grove , Garden)
Plains = Environment (Desert , Tundra , Badlands , Temple)
Grasslands = Environment (Prarie , Meadow , Swamp , Fort)
Waterlands = Environment (Lake , Beach , Island , Shipwreck)
Rockylands = Environment (Mountain , Canyon , Cave , Monument)
