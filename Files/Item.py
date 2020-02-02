"""
Item.py
NewScript
"""


class Item:
    def __init__(self, name, recipe, rarity, reference, craft_log, expendable=False):
        self.name = name
        self.recipe = recipe
        self.rarity = rarity
        self.expendable = expendable
        self.is_weapon = False

        craft_log[self] = self.recipe

        # Plural:
        if name[-1] in ["s", "x", "z"] or name[-2:] in ["ss", "sh", "ch"]:
            self.plural = name + "es"
        elif name[-1] == "y":
            self.plural = name[:-1] + "ies"
        else:
            self.plural = name + "s"
            
        reference[self.name] = self
        reference[self.plural] = self
