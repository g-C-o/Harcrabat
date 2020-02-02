"""
Projectile.py
NewScript
"""

from Weapon import Weapon

class Projectile(Weapon):
    def __init__(self, name, recipe, launcher, damage, rarity, reference):
        super().__init__(name, recipe, "Projectile", None, None, damage, None, False, rarity, "fire", "fired", reference, expendable=True)
        self.launcher = launcher