"""
Environment.py
Harcrabat
"""


from Database import ENVIRONMENT_NAMES, ENV_INCONSISTENCY, ENV_CLUSTER_SIZE
import Biome
from random import choices


class Environment:
	def __init__(self, type, primary_biome, secondary_biome, tertiary_biome, abandoned_structure):
		self.pri_B = primary_biome
		self.sec_B = secondary_biome
		self.ter_B = tertiary_biome
		self.structure = abandoned_structure



class Woodlands(Environment):

	
	def __init__(self):

		self.type = "Woodlands"
		self.pri_B = Biome.Forest
		self.sec_B = Biome.Jungle
		self.ter_B = Biome.Grove
		self.structure = Biome.Garden

		Environment.__init__(type, pri_B, sec_B, ter_B, structure)



class Plains(Environment):

	
	def __init__(self):

		self.type = "Plains"
		self.pri_B = Biome.Desert
		self.sec_B = Biome.Tundra
		self.ter_B = Biome.Badland
		self.structure = Biome.Temple

		Environment.__init__(type, pri_B, sec_B, ter_B, structure, *args, **kwargs)



class Grasslands(Environment):

	
	def __init__(self):

		self.type = "Grasslands"
		self.pri_B = Biome.Prairie
		self.sec_B = Biome.Meadow
		self.ter_B = Biome.Swamp
		self.structure = Biome.Fort

		Environment.__init__(type, pri_B, sec_B, ter_B, structure, *args, **kwargs)



class Waterlands(Environment):

	
	def __init__(self):

		self.type = "Waterlands"
		self.pri_B = Biome.Lake
		self.sec_B = Biome.Beach
		self.ter_B = Biome.Island
		self.structure = Biome.Shipwreck

		Environment.__init__(type, pri_B, sec_B, ter_B, structure, *args, **kwargs)



class Rockylands(Environment):

	
	def __init__(self):

		self.type = "Rockylands"
		self.pri_B = Biome.Mountain
		self.sec_B = Biome.Canyon
		self.ter_B = Biome.Cave
		self.structure = Biome.Monument

		Environment.__init__(type, pri_B, sec_B, ter_B, structure, *args, **kwargs)