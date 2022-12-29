import json

def author(command):
    if command == "author":
        data = open("author.json",mode="r",encoding="utf-8")
        return json.load(data)