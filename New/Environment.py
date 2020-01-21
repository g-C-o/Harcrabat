"""
Environment.py
NewScript
"""


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
