"""
Environment.py
Harcrabat
"""


from Database import ENVIRONMENTS, ENV_INCONSISTENCY, ENV_CLUSTER_SIZE
import Biome
from random import choices


class Environment:
	def __init__(self, type, primary_biome, secondary_biome, tertiary_biome, abandoned_structure):
		self.pri_B = primary_biome
		self.sec_B = secondary_biome
		self.ter_B = tertiary_biome
		self.structure = abandoned_structure


	def choose(surroundings):
		surroundings = [Square for Square in surroundings if Square] 
		env_probs = {Env: ENV_INCONSISTENCY for Env in ENVIRONMENTS}
		for Square in surroundings:
			env_probs [Square] = env_probs [Square] * ENV_CLUSTER_SIZE
		env_weights = [prob for prob in list(env_probs.values())]
		EnvChoice = choices(ENVIRONMENTS, weights=env_weights) [0]
		return EnvChoice



class Woodlands(Environment):

	
	def __init__(self):

		self.type = "Woodlands"
		self.pri_B = Biome.Forest
		self.sec_B = Biome.Jungle
		self.ter_B = Biome.Grove
		self.structure = Biome.Garden

		Environment.__init__(*args, **kwargs)



class Plains(Environment):

	
	def __init__(self):

		self.type = "Plains"
		self.pri_B = Biome.Desert
		self.sec_B = Biome.Tundra
		self.ter_B = Biome.Badland
		self.structure = Biome.Temple

		Environment.__init__(*args, **kwargs)



class Grasslands(Environment):

	
	def __init__(self):

		self.type = "Grasslands"
		self.pri_B = Biome.Prairie
		self.sec_B = Biome.Meadow
		self.ter_B = Biome.Swamp
		self.structure = Biome.Fort

		Environment.__init__(*args, **kwargs)



class Waterlands(Environment):

	
	def __init__(self):

		self.type = "Waterlands"
		self.pri_B = Biome.Lake
		self.sec_B = Biome.Beach
		self.ter_B = Biome.Island
		self.structure = Biome.Shipwreck

		Environment.__init__(*args, **kwargs)



class Rockylands(Environment):

	
	def __init__(self):

		self.type = "Rockylands"
		self.pri_B = Biome.Mountain
		self.sec_B = Biome.Canyon
		self.ter_B = Biome.Cave
		self.structure = Biome.Monument

		Environment.__init__(*args, **kwargs)