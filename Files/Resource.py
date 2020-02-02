"""
Resource.py
NewScript
"""

from Item import Item

class Resource(Item):
    def __init__(self, name, rarity, reference, *args):
        super().__init__(name, None, rarity, reference, *args)
