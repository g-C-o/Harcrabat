from Database import *
from Game import *
from random import randint , choice
####import Image

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

def create_player ():
    DesiredName = input ("Enter your name:\n| ")
    eval (PrintSeparater)
    Player .set_name (DesiredName)

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
