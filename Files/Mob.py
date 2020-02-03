"""
Mob.py
NewScript
"""


class Mob:
    def __init__(self, name, category, health, x, y):
        self.name = name
        self.type = category
        self.health = health
        self.x = x
        self.y = y

class Fighter(Mob):
    def __init__(self, *args):
        super().__init__("Fighter", "Hostile", 50, *args)

class Predator(Mob):
    def __init__(self, *args):
        super().__init__("Predator", "Hostile", 50, *args)

class Goblin(Mob):
    def __init__(self, *args):
        super().__init__("Goblin", "Hostile", 50, *args)

class Destroyer(Mob):
    def __init__(self, *args):
        super().__init__("Destroyer", "Hostile", 50, *args)

class Annihilator(Mob):
    def __init__(self, *args):
        super().__init__("Annihilator", "Hostile", 50, *args)

class Troll(Mob):
    def __init__(self, *args):
        super().__init__("Troll", "Hostile", 50, *args)

class Raider(Mob):
    def __init__(self, *args):
        super().__init__("Raider", "Hostile", 50, *args)

class Minion(Mob):
    def __init__(self, *args):
        super().__init__("Minion", "Hostile", 50, *args)

class Zombie(Mob):
    def __init__(self, *args):
        super().__init__("Zombie", "Hostile", 50, *args)

class Defender(Mob):
    def __init__(self, *args):
        super().__init__("Defender", "Hostile", 50, *args)

class Guardian(Mob):
    def __init__(self, *args):
        super().__init__("Guardian", "Hostile", 50, *args)

class Skeleton(Mob):
    def __init__(self, *args):
        super().__init__("Skeleton", "Hostile", 50, *args)

class Hunter(Mob):
    def __init__(self, *args):
        super().__init__("Hunter", "Hostile", 50, *args)

class Assasin(Mob):
    def __init__(self, *args):
        super().__init__("Assasin", "Hostile", 50, *args)

class Ghoul(Mob):
    def __init__(self, *args):
        super().__init__("Ghoul", "Hostile", 50, *args)