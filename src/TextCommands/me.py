import json
def me(command,displayName,pictureUrl,statusMessage):
    if command == "me":
        with open("me.json",mode="r",encoding="utf-8") as file:
            data = json.load(file)
            i = 0
            data["hero"]["url"]=pictureUrl
            data["body"]["contents"][0]["text"] = displayName
            data["body"]["contents"][1]["text"] = statusMessage
        
        with open("me.json",mode="w",encoding="utf-8") as file:
            json.dump(data,open("me.json",mode="w",encoding="utf-8"))

        return json.load(open("me.json",mode="r",encoding="utf-8"))