"""
Biome.py
NewScript
"""

from Database import BIOME_WEIGHTS, RESOURCE_WEIGHTS, HARVEST_SIZE
from random import choices


class Biome:
    def __init__(self, name, preposition, primary_resource, secondary_resource, tertiary_resource, primary_mob, secondary_mob, tertiary_mob, animal, primary_loot, secondary_loot, rarity):
        self.name = name
        self.preposition = preposition
        self.pri_R = primary_resource
        self.sec_R = secondary_resource
        self.ter_R = tertiary_resource
        self.pri_M = primary_mob
        self.sec_M = secondary_mob
        self.ter_M = tertiary_mob
        self.animal = animal
        self.pri_L = primary_loot
        self.sec_L = secondary_loot
        self.rarity = rarity

    def choose(game, Env):
        EnvClass = eval("game." + Env)
        BiomeChoice = choices([EnvClass.pri_B, EnvClass.sec_B,
                               EnvClass.ter_B, EnvClass.structure], weights=BIOME_WEIGHTS)[0]
        return BiomeChoice

    def gen_resources(self):
        new_resources = choices(
            [self.pri_R, self.sec_R, self.ter_R], weights=RESOURCE_WEIGHTS, k=HARVEST_SIZE)
        return new_resources
