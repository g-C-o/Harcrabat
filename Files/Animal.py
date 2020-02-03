"""
Animal.py
NewScript
"""

from Mob import Mob

class Animal(Mob):
    def __init__(self, *args):
        super().__init__(*args)

class Chicken(Animal):
    def __init__(self, *args):
        super().__init__("Chicken", "Animal", 20, *args)
        
class Rabbit(Animal):
    def __init__(self, *args):
        super().__init__("Rabbit", "Animal", 20, *args)

class Cow(Animal):
    def __init__(self, *args):
        super().__init__("Cow", "Animal", 20, *args)
        
class Fish(Animal):
    def __init__(self, *args):
        super().__init__("Fish", "Animal", 20, *args)

class Sheep(Animal):
    def __init__(self, *args):
        super().__init__("Sheep", "Animal", 20, *args)