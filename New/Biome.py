"""
Biome.py
NewScript
"""

        
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


    def gen_resources (self):
        NewResources = choices ([self.GroundR , self.PriR , self.SecR , self.TerR] , weights=ResourceWeights , k = 5)
        return NewResources
