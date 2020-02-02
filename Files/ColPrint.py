"""
ColPrint
A basic print module to print text in multiple columns

:version: v1.0
:author: Dallin Guisti
:date: 1/31/2020

Designed for Python Version 3.7.x

"""

from itertools import zip_longest
from Database import PRINT_COLORS

def colprint(titles, list1, list2):
    spaceLen = len(max(list1, key=len))
    print(titles[0], ''.join([" " for _ in range(spaceLen - len(titles[0]))]), "", titles[1])
    for one, two in zip_longest(list1, list2):
        lengthMod = 0
        if one != None:
            for key in PRINT_COLORS.keys():
                if PRINT_COLORS[key] in one:
                    if key != "Reset":
                        lengthMod = len(PRINT_COLORS[key])
                        break

        if one == None: 
            print(" ", ''.join([" " for _ in range(spaceLen + 2 + lengthMod)]), "", two)
        elif two == None:
            print("  ", one)
        else:
            print("  ", one, ''.join([" " for _ in range(spaceLen - len(one) + 4 + lengthMod)]), "", two)

if __name__ == "__main__":
    colprint(["Title 1", "Title 2"], ["Itdsfdsfem " + str(num) for num in range(10)], ["Item " + str(num2) for num2 in range(14)])