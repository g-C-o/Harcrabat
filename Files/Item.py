"""
Item.py
NewScript
"""


class Item:
    def __init__(self, name, recipe):
        #### self.name = name
        self.recipe = recipe
        self.name = name
        # Add Rarity calculation:
        # Average Resource rarity
        # divided by number of resources?


class Weapon(Item):
    def __init__(self, name, recipe, damage, durabiliy, wrange):
        super().__init__(name, recipe)

        def attack(self, target):
            print("Attacking", target.name)
