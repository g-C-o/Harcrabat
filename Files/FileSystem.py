"""
FileSystem.py
NewScript
Controls all saving and loading of file system data
"""
import calendar
import time
import datetime
from os import path
import os

class SC_ERRORS:
    bug = 0
    glitch = 1
    failure = 2
    test = -1

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
        if "inventory" in data.keys():
            with open(self.path + "inventory.nsd", "w") as f:
                for item in data["inventory"]:
                    amount = data["inventory"][item]
                    print(item.name + "-" + str(amount), file=f)
                    
        if "plyrinfo" in data.keys():
            with open(self.path + "plyrinfo.nsd", "w") as f:
                if "name" in data["plyrinfo"].keys():
                    print("name" + "-" + data["plyrinfo"]["name"], file=f)

        self.log("Data saved to file.")

    def log(self, text):
        try:
            with open(self.path + "output.log", "a") as f:
                ts = calendar.timegm(time.gmtime())
                readable = datetime.datetime.fromtimestamp(ts).isoformat()
                print("", file=f)
                print(readable, file=f)
                print(text, file=f)
        except FileNotFoundError:
            try:
                with open(self.path + "output.log", "w") as f:
                    ts = calendar.timegm(time.gmtime())
                    readable = datetime.datetime.fromtimestamp(ts).isoformat()
                    print("", file=f)
                    print(readable, file=f)
                    print(text, file=f)
            except FileNotFoundError:
                os.system("cd " + self.path + "../")
                os.system("mkdir Savefiles")
                os.system("cd " + self.path + "../Files")
                with open(self.path + "output.log", "w") as f:
                    ts = calendar.timegm(time.gmtime())
                    readable = datetime.datetime.fromtimestamp(ts).isoformat()
                    print("", file=f)
                    print(readable, file=f)
                    print(text, file=f)

    def error(self, etype, tb, info=None):
        self.log("Error code " + str(etype))
        if etype == 0:
            textType = "bug"
        elif etype == 1:
            textType = "glitch"
        elif etype == 2:
            textType = "failure"
        elif etype == -1:
            textType = "test"
        else:
            textType = "unknown"
        try:
            with open(self.path + "errors.log", "a") as f:
                ts = calendar.timegm(time.gmtime())
                readable = datetime.datetime.fromtimestamp(ts).isoformat()
                print("", file=f)
                print(readable, file=f)
                print("Error of type " + textType + ".", file=f)
                print("Traceback:\n" + tb, file=f)
                if info:
                    print("Additional info:\n" + info, file=f)
        except FileNotFoundError:
            with open(self.path + "errors.log", "w") as f:
                ts = calendar.timegm(time.gmtime())
                readable = datetime.datetime.fromtimestamp(ts).isoformat()
                print("", file=f)
                print(readable, file=f)
                print("Error of type " + textType +  ".", file=f)
                print("Traceback:\n" + tb, file=f)
                if info:
                    print("Additional info:\n" + info, file=f)
                
#if __name__ == "__main__":
#    filesystem = FileSystem("..\Savefiles\\")
#    print(filesystem.load())
