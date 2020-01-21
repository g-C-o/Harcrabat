"""
Character.py
NewScript
"""


class Character:
    def __init__(self , Name , Score , Map , BiomeMap , CollectTimeMap ,  Health , Energy , Inventory , HandItem , Armor , Location , Orientation , LastMoveTime):
        self .Name = Name
        self .Score = Score
        self .Map = Map
        self .BiomeMap = BiomeMap
        self .CollectTimeMap = CollectTimeMap
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
        if time () - self .CollectTimeMap [self .Location [0]-1] [self .Location [1]-1] < CollectDelay: return
        NewResources = self .BiomeMap [self.Location[0]-1][self.Location[1]-1] .gen_resources ()
        self .CollectTimeMap [self .Location [0]-1] [self .Location [1]-1] = time ()
        print ("You harvested new resources:")
        DisplayedResources = []
        for NewResource in NewResources:
            try : Player .Inventory [NewResource] += 1
            except KeyError : Player .Inventory [NewResource] = 1
            if NewResource in DisplayedResources: continue
            else:
                DisplayedResources .append (NewResource)
                if NewResources .count (NewResource) == 1:
                    ResourceName = NewResource .Name
                else: ResourceName = NewResource .Plural
                print ("\t%i %s%s" % (NewResources.count(NewResource) , PrintColors [NewResource.Rarity] , ResourceName) + Style.RESET_ALL)
        

    def attack (self):
        print ("attack")


    def list_inv (self):
        print ("Inventory:")
        for Resource in self. Inventory:
            if self .Inventory [Resource] == 1:
                ResourceName = Resource .Name
            else: ResourceName = Resource .Plural
            print ("\t" + str(self.Inventory[Resource]) + " " + PrintColors[Resource.Rarity] + ResourceName + PrintColors["Reset"])
