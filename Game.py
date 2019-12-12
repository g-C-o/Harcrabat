""" The file that contains the game mechanics """

import msvcrt
from Database import *

### START CODE ###

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
    BiomeMap = [[Biome .choose (Env)
        for Env in Row]
        for Row in Map]
    
    Player .Map = Map
    Player .BiomeMap = BiomeMap

    return Map , BiomeMap


def run_game ():
    ## Wait for keypress:
    while True:
        while not msvcrt .kbhit ():
            pass
            #### Update game
        KeyInput = msvcrt .getch ()
        
        ## Respond to keypress:
        if KeyInput in KeyBindings:
            eval (KeyBindings [KeyInput][0])

def update_game ():
    pass
    #### Update health and energy
    #### Regenerate resources in exhausted squares
    #### Spawn stuff
        
