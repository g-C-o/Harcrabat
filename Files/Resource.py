"""
Resource.py
NewScript
"""


class Resource:
    def __init__(self, name, rarity, reference):
        self.name = name
        self.rarity = rarity
        self.is_weapon = False

        # Plural:
        if name[-1] in ["s", "x", "z"] or name[-2:] in ["ss", "sh", "ch"]:
            self.plural = name + "es"
        elif name[-1] == "y":
            self.plural = name[:-1] + "ies"
        else:
            self.plural = name + "s"
            
        reference[self.name] = self
        reference[self.plural] = self
