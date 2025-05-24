import random

enemies_list = []

def spawn(sprites, type):
    new_enemy = {
        "TYPE": type.upper(),
        "X": random.randint(0, 800), 
        "Y": random.randint(0, 800),
    }
    
    if new_enemy["TYPE"] == "JAVALI":
        new_enemy["HP"] = 150
        new_enemy["SPRITE"] = sprites["JAVALI"]
    elif new_enemy["TYPE"] == "LENHADOR":
        new_enemy["HP"] = 100
        new_enemy["SPRITE"] = sprites["LENHADOR"]
    elif new_enemy["TYPE"] == "CACADOR":
        new_enemy["HP"] = 100
        new_enemy["SPRITE"] = sprites["CACADOR"]
    
    enemies_list.append(new_enemy)
