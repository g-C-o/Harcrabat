from NewScript import command_input
from time import time
from random import choices
import msvcrt


### VARIABLES ###


PrintSeparater = "print ('-----------------------------------------------')"
EnvCleanupFactor = 50
EnvInconsistency = 1.01
EnvClusterSize = 5
CollectDelay = 60
MoveDelay = 5
Red = '\033[31m'
Green = '\033[32m'
Blue = '\033[34m'
White = '\033[37m'
Black = '\033[30m'

Environments = ["Woodlands" , "Plains" , "Grasslands" , "Waterlands" , "Rockylands"]
BiomeWeights = [60 , 20 , 5 , 1]

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
    }

    
### CLASS DEFINITIONS ###   
    
    
class Character:
    def __init__(self , Name , Score , Map , BiomeMap , CollectTimeMap ,  Health , Energy , Inventory , HandItem , Armor , Location , Orientation , LastMoveTime):
        self .Name = Name
        self .Score = Score
        self .Map = Map
        self .BiomeMap = BiomeMap
        self .Health = Health
        self .Energy = Energy
        self .Inventory = Inventory
        self .HandItem = HandItem
        self .Armor = Armor
        self .Location = Location
        self .Orientation = Orientation
        self .LastMoveTime = LastMoveTime
        

    def look (self):
        try:
            if self .Orientation  == "North":
                BiomeAhead = self .BiomeMap [self.Location[0]-2][self.Location[1]-1] .Name 
            elif self .Orientation  == "South":
                BiomeAhead = self .BiomeMap [self.Location[0]][self.Location[1]-1] .Name 
            elif self .Orientation  == "West":
                BiomeAhead = self .BiomeMap [self.Location[0]-1][self.Location[1]-2] .Name 
            elif self .Orientation  == "East":
                BiomeAhead = self .BiomeMap [self.Location[0]-1][self.Location[1]] .Name 
            for Index , Coord in enumerate (self .Location):
                if Coord < 0 or Coord > 50:
                    raise IndexError
            Article = eval (BiomeAhead) .Preposition [5:]
            print ("You look %s and see %s %s." % (self.Orientation , Article , BiomeAhead))            
        except IndexError:
            print ("You see the edge of the world.")

        
    def describe_spawnpoint (self):
        CurrentBiome = self .BiomeMap [26][26] .Name
        AltPreposition = eval (CurrentBiome) .Preposition [:2] + eval (CurrentBiome) .Preposition [4:]
        print ("You spawn %s %s. You are facing North." % (AltPreposition , CurrentBiome))


    def describe_surroundings (self):
        CurrentBiome = self .BiomeMap [self.Location[0]-1][self.Location[1]-1] .Name
        CurrentEnv = self .Map [self.Location[0]-1][self.Location[1]-1]
        print ("Current Location:")
        print ("\tCoordinates: " + str(self.Location))
        print ("\tEnvironment: " + CurrentEnv)
        print ("\tBiome: " + CurrentBiome)

    
    def set_name (self, NewName):
        self .Name = NewName

    def switch_hand_item (self, NewItem):
        self .HandItem = NewItem

        
    def switch_armor (self, NewArmor):
        self .Armor = NewArmor

    
    def move (self):
        if time () - self .LastMoveTime < MoveDelay: return
        try:
            if self .Orientation  == "North":
                self .Location [0] -= 1
            elif self .Orientation  == "South":
                self .Location [0] += 1
            elif self .Orientation  == "West":
                self .Location [1] -= 1
            elif self .Orientation  == "East":
                self .Location [1] += 1
            for Index , Coord in enumerate (self .Location):
                if Coord < 0:
                    self .Location [Index] = 0
                elif Coord > 50:
                    self .Location [Index] = 50
                else: continue
                raise IndexError
            CurrentBiome = self .BiomeMap [self.Location[0]-1][self.Location[1]-1] .Name
            self .LastMoveTime = time ()
            print ("You move %s %s %s." % (self.Orientation , eval(CurrentBiome).Preposition , CurrentBiome))            
        except IndexError:
            print ("You have reached the edge of the world.")


    def turn (self , NewOrientation):
        self .Orientation = NewOrientation
        print ("You turn to the %s." % NewOrientation)


    def collect (self):
        print ("collect")


    def attack (self):
        print ("attack")

        
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
    def __init__ (self , Name , Preposition , Ground , PrimaryResource , SecondaryResource , TertiaryResource , PrimaryMob , SecondaryMob , TertiaryMob , Animal , PrimaryLoot , SecondaryLoot):
        self .Name = Name
        self .Preposition = Preposition
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


#### INSTANCES ###


## Player:    
Player = Character ("Player 1" , 0 , [] , [] , [[time() - CollectDelay for Square in range (50)] for Row in range (50)] , 100 , 100 , {} , None , None , [26,26] , "North" , time())

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
Forest = Biome ("Forest" , "into a" , Soil , Wood , Leaves , Bark , Fighter , Fighter , Fighter , Chicken , None , None)
Jungle = Biome ("Jungle" , "into a" , Soil , Wood , Vines , Moss , Fighter , Fighter , Predator , Chicken , None , None)
Grove = Biome ("Grove" , "into a" , Soil , Wood , Fruit , Rocks , Fighter , Predator , Fighter , Chicken , None , None)
Garden = Biome ("Garden" , "into a" , Soil , Fruit , Gravel , Water , Fighter , Predator , Goblin , Chicken , HarvesterArmor , Protector)
Desert = Biome ("Desert" , "into a" , Sand , Rocks , Cacti , Iron , Destroyer , Destroyer , Destroyer , Rabbit , None , None)
Tundra = Biome ("Tundra" , "into a" , Snow , Rocks , Iron , Wood , Destroyer , Destroyer , Annihilator , Rabbit , None , None)
Badland = Biome ("Badland" , "into a" , Sand , Snow , Bones , Diamonds , Destroyer , Annihilator , Destroyer , Rabbit , None , None)
Temple = Biome ("Temple" , "into a" , Sand , Iron , Wood , Gold , Destroyer , Annihilator , Troll , Rabbit , Strawman , Coffin)
Prairie = Biome ("Prairie" , "into a" , Soil , Gravel , Stone , Iron , Raider , Raider , Raider , Cow , None , None)
Meadow = Biome ("Meadow" , "into a" , Soil , Flowers , Clay , Gold , Raider , Raider , Minion , Cow , None , None)
Swamp = Biome  ("Swamp" , "into a" , Mud , Water , Gold , Iron , Raider , Minion , Raider , Cow , None , None)
Fort = Biome ("Fort" , "into a" , Wood , Stone , Iron , Diamonds , Raider , Minion , Zombie , Cow , Ladder , MobRepellant)
Lake = Biome ("Lake" , "into a" , Water , Soil , Rocks , Emeralds , Defender , Defender , Defender , Fish , None , None)
Beach = Biome ("Beach" , "into a" , Water , Sand , Clay , Emeralds , Defender , Defender , Guardian , Fish , None , None)
Island = Biome ("Island" , "onto an" , Soil , Iron , Water , Quartz , Defender , Guardian , Defender , Fish , None , None)
Shipwreck = Biome ("Shipwreck" , "into a" , Wood , Water , Gold , Quartz , Defender , Guardian , Skeleton , Fish , BottledWave , BottledWind)
Mountain = Biome ("Mountain" , "onto a" , Stone , Soil , Wood , Quartz , Hunter , Hunter , Hunter , Sheep , None , None)
Canyon = Biome ("Canyon" , "into a" , Stone , Gravel , Leaves , Quartz , Hunter , Hunter , Assasin , Sheep , None , None)
Cave = Biome ("Cave" , "into a" , Stone , Iron , Wood , Quartz , Hunter , Assasin , Hunter , Sheep , None , None)
Monument = Biome ("Monument" , "into a" , Iron , Stone , Diamonds , Gravel , Hunter , Assasin , Ghoul , Sheep , Gliders , Binoculars)

## Environments:
Woodlands = Environment (Forest , Jungle , Grove , Garden)
Plains = Environment (Desert , Tundra , Badland , Temple)
Grasslands = Environment (Prairie , Meadow , Swamp , Fort)
Waterlands = Environment (Lake , Beach , Island , Shipwreck)
Rockylands = Environment (Mountain , Canyon , Cave , Monument)
