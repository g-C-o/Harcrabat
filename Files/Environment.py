"""
Environment.py
NewScript
"""


from Database import ENVIRONMENTS, ENV_INCONSISTENCY, ENV_CLUSTER_SIZE
from random import choices


class Environment:
	def __init__(self, primary_biome, secondary_biome, tertiary_biome, abandoned_structure):
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
