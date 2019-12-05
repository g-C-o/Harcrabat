from Database import *
from Extras import *
from Game import *
from random import randint , choice
import Image

### FUNCTIONS ###

def startup ():
    print ("NewScript Version 3")
    print ("Type 'help' for the command list.")
    while True:
        command_input ()

def command_input ():
    eval (PrintSeparater)
    Command = (input ("| ")) .lower ()
    eval (PrintSeparater)
    if Command in Commands : eval (Command + "()")
    else : print ("Invalid Command")

def load_map ():
    print ("Loading Map")

    ## Preload Map:
    print ("\tCreating Seed")
    Map = [[None 
            if ColIndex in [0,51]
            or RowIndex in [0,51]
            else choices (("Woodlands" , "Plains" , "Grasslands" , "Waterlands" , "Rockylands")) [0]
        for ColIndex in range (52)]
        for RowIndex in range (52)]
    
    ## Choose Environments:
    print ("\tGenerating Chunks")
    for Rep in range (EnvCleanupFactor):
        Map = [[None
                if ColIndex in [0,51]
                or RowIndex in [0,51]
                else Environment .choose ([Map[RowIndex-1][ColIndex-1] , Map[RowIndex-1][ColIndex] , Map[RowIndex-1][ColIndex+1] , Map[RowIndex][ColIndex-1] , Map[RowIndex][ColIndex+1] , Map[RowIndex+1][ColIndex-1] , Map[RowIndex+1][ColIndex] , Map[RowIndex+1][ColIndex+1]])
            for ColIndex in range(len(Map[RowIndex]))]
            for RowIndex in range(len(Map))]
    Map = [[Env for Env in Row[1:-1]] for Row in Map[1:-1]]

    ## Choose Biomes:
    print ("\tGenerating Terrain")
    Map = [[Biome .choose (Env)
        for Env in Row]
        for Row in Map]

    return Map

def create_player ():
    DesiredName = input ("Enter your name:\n| ")
    eval (PrintSeparater)
    Player .set_name (DesiredName + " wishes he or she was Cameron")

### COMMANDS ###

def help ():
    [print (Command+ ": " + Commands[Command]) for Command in Commands]

def start ():
    create_player ()
    Map = load_map ()
    run_game ()
    
    #### Spawn function (set location and stats)
    #### run_game () (will endlessly update game while waiting for input)

if __name__ == "__main__" : startup ()
else : pass #### Check for CorPC sample name.
