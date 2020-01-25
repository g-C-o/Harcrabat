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
        self.log("New Game Initiated")

    def load(self):
        myData = {}
        if path.exists(self.path + "inventory.nsd"):  # NSD - NewScriptData
            with open(self.path + "inventory.nsd", "r") as f:
                myData["inventory"] = [
                    tuple(y.replace("\n", "").split("-")) for y in f.readlines()]

        if path.exists(self.path + "plyrinfo.nsd"):  # NSD - NewScriptData
            with open(self.path + "plyrinfo.nsd", "r") as f:
                file = [tuple(y.replace("\n", "").split("-"))
                        for y in f.readlines()]
                myData["plyrinfo"] = dict(file)
        return myData

    def save(self, data):
        with open(self.path + "inventory.nsd", "w") as f:
            for item in data["inventory"]:
                amount = data["inventory"][item]
                print(item.name + "-" + str(amount), file=f)

        with open(self.path + "plyrinfo.nsd", "w") as f:
            if data["plyrinfo"]["name"] != "Player 1":
                print("name" + "-" + data["plyrinfo"]["name"], file=f)

        self.log("Data saved to file.")

    def log(self, text):
        with open(self.path + "output.log", "a") as f:
            ts = calendar.timegm(time.gmtime())
            readable = datetime.datetime.fromtimestamp(ts).isoformat()
            print("", file=f)
            print(readable, file=f)
            print(text, file=f)


if __name__ == "__main__":
    filesystem = FileSystem("..\\Savefiles\\")
    print(filesystem.load())
