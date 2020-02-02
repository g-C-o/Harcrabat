"""
Weapon.py
NewScript
"""

from Item import Item

class Weapon(Item):
    def __init__(self, name, recipe, type, speed, accuracy, damage, range, has_scope, rarity, action_word, action_word_pt, reference, *args, expendable=False):
        super().__init__(name, recipe, rarity, reference, *args)
        self.type = type
        self.speed = speed
        self.accuracy = accuracy
        self.damage = damage
        self.range = range
        self.has_scope = has_scope
        self.action_word = action_word
        self.action_word_pt = action_word_pt
        self.is_weapon = True
        
    def attack(self, target):
            if target == None:
                tname = "thin air"
            else:
                tname = target.name

            print("You", self.action_word, "your",
                  self.name.lower(), "at", tname + ".")
