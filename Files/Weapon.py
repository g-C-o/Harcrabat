"""
Weapon.py
NewScript
"""


class Weapon:
    def __init__(self, name, recipe, type, speed, accuracy, damage, range, has_scope, rarity, action_word, action_word_pt, reference, expendable=False):
        self.name = name
        self.recipe = recipe
        self.type = type
        self.speed = speed
        self.accuracy = accuracy
        self.damage = damage
        self.range = range
        self.has_scope = has_scope
        self.rarity = rarity
        self.action_word = action_word
        self.action_word_pt = action_word_pt
        self.is_weapon = True
        self.expendable = expendable

        # Plural:
        if name[-1] in ["s", "x", "z"] or name[-2:] in ["ss", "sh", "ch"]:
            self.plural = name + "es"
        elif name[-1] == "y":
            self.plural = name[:-1] + "ies"
        else:
            self.plural = name + "s"
        
        reference[self.name] = self
        reference[self.plural] = self
        
    def attack(self, target):
            if target == None:
                tname = "thin air"
            else:
                tname = target.name

            print("You", self.action_word, "your",
                  self.name.lower(), "at", tname + ".")
