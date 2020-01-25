"""
Item.py
NewScript
"""


class Item:
    def __init__(self, name, recipe):
        #### self.name = name
        self.recipe = recipe
        self.name = name
        self.is_weapon = False
        # Add Rarity calculation:
        # Average Resource rarity
        # divided by number of resources?


class Weapon(Item):
    def __init__(self, name, recipe, damage, durabiliy, wrange, action_word, action_word_pt):
        super().__init__(name, recipe)
        self.is_weapon = True
        self.action_word = action_word
        self.damage = damage
        self.range = wrange
        self.action_word = action_word
        self.action_word_pt = action_word_pt

        def attack(self, target):
            if target == None:
                tname = "thin air"
            else:
                tname = target.name

            print("You", self.action_word, "your",
                  self.name.lower(), "at", tname + ".")
