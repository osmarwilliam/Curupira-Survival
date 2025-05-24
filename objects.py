import random

objects_list = []

def spawn(sprites, type):
    new_object = {
        "TYPE": type.upper(),
        "X": random.randint(0, 800), 
        "Y": random.randint(0, 800),
    }
    
    if new_object["TYPE"] == "BAU":
     new_object["SPRITE"] = sprites["BAU"]
    elif new_object["TYPE"] == "COMIDA":
     new_object["SPRITE"] = sprites["COMIDA"]
    elif new_object["TYPE"] == "RELOGIO":
     new_object["SPRITE"] = sprites["RELOGIO"]

    objects_list.append(new_object)
