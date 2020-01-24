"""
FileSystem.py
NewScript
Controls all saving and loading of file system data
"""
import calendar
import time
import datetime
from os import path


class FileSystem:
    def __init__(self, myPath):
        self.path = myPath
        """
        with open(self.path + "output.log", "a") as f:
            ts = calendar.timegm(time.gmtime())
            readable = datetime.datetime.fromtimestamp(ts).isoformat()
            print("", file=f)
            print(readable, file=f)
            print("New Game Initiated", file=f)#"""

    def load(self):
        myData = {}
        if path.exists(self.path + "inventory.nsd"): # NSD - NewScriptData
            with open(self.path + "inventory.nsd", "r") as f:
                myData["inventory"] = [tuple(y.replace("\n", "").split("-")) for y in f.readlines()]
        return myData

    def save(self, data):
        with open(self.path + "inventory.nsd", "w") as f: 
            for item in data["inventory"]:
                amount = data["inventory"][item]
                print(item.name + "-" + str(amount), file=f)

if __name__ == "__main__":
    filesystem = FileSystem(".\\Savefiles\\")
    print(filesystem.load())