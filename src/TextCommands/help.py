import json

def help(command):
    if command == "help":
        data = open("C:\\Users\\User\\Documents\\GitHub\\Hual_Bot\\src\\Data\\help.json",mode="r",encoding="utf-8")
        return json.load(data)