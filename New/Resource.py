"""
Resource.py
NewScript
"""


class Resource:
    def __init__ (self , Name , Frequency , Plural):
        self .Name = Name
        self .Plural = Plural
        
        if Frequency <= 16 : self .Rarity = "Rare"
        elif Frequency <= 80 : self .Rarity = "Uncommon"
        else : self .Rarity = "Common"
        
        if Name [-1] in ["s","x","z"] or Name [-2:] in ["ss","sh","ch"]:
               self .Plural = Name + "es"
        elif Name [-1] == "y": self .Plural = Name [:-1] + "ies"
        else:
               self .Plural = Name + "s"
