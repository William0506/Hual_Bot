import json

def author(command):
    if command == "author":
        data = open("C:\\Users\\User\\Documents\\GitHub\\Hual_Bot\\src\\Data\\author.json",mode="r",encoding="utf-8")
        return json.load(data)