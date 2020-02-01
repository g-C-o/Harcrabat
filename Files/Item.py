"""
Item.py
NewScript
"""


class Item:
    def __init__(self, name, recipe, rarity, reference):
        self.name = name
        self.recipe = recipe
        self.rarity = rarity
        self.is_weapon = False
        if name[-1] in ["s", "x", "z"] or name[-2:] in ["ss", "sh", "ch"]:
            self.plural = name + "es"
        elif name[-1] == "y":
            self.plural = name[:-1] + "ies"
        else:
            self.plural = name + "s"
            
        reference[self.name] = self
        reference[self.plural] = self
