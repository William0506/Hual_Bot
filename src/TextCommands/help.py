import json

def help(command):
    if command == "help":
        data = open("help.json",mode="r",encoding="utf-8")
        return json.load(data)