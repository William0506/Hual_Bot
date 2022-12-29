import random

def g (command,user_name) :
    if command == "g":
        return random.choice(["Hi!","Hello!","Hey!there!","你好!","嗨!"])+str(user_name)