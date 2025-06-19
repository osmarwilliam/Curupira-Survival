import random

from PPlay.sprite import *

objects_list = []

def spawn(type):
    new_object = {
        "TYPE": type.upper(),
        "X": random.randint(0, 800), 
        "Y": random.randint(0, 800),
    }
    
    if new_object["TYPE"] == "BAU":
     new_object["SPRITE"] = Sprite("assets/bau.png")
    elif new_object["TYPE"] == "COMIDA":
     new_object["SPRITE"] = Sprite("assets/comida.png")
    elif new_object["TYPE"] == "RELOGIO":
     new_object["SPRITE"] = Sprite("assets/relogio.png")

    objects_list.append(new_object)

def arrow_spawn(x, y, target_x, target_y):
    dx = target_x - x
    dy = target_y - y
    distancia = (dx**2 + dy**2)**0.5

    if distancia == 0: # Evita divisão por 0
        dir_x, dir_y = 0,0
    else:
        dir_x = dx / distancia
        dir_y = dy / distancia

    new_arrow = {
        "TYPE": "ARROW",
        "SPEED": 300,
        "X": x,
        "Y": y,
        "DIR_X": dir_x,
        "DIR_Y": dir_y,
        "SPRITE": Sprite("assets/flecha.png")
    }
    
    objects_list.append(new_arrow)

def drop_xp(enemy):
    xp_drop = {
        "TYPE": "XP",
        "X": enemy["X"],
        "Y": enemy["Y"],
        "SPRITE": Sprite("assets/xp.png", frames = 4)
    }
    xp_drop["SPRITE"].set_total_duration(300)

    if enemy["TYPE"] == "JAVALI": # Dropa 5 XP
        xp_drop["VALUE"] = 5
    elif enemy["TYPE"] == "LENHADOR": # Dropa 10 xp
        xp_drop["VALUE"] = 10
    elif enemy["TYPE"] == "CACADOR": # Dropa 20 xp
        xp_drop["VALUE"] = 15
    
    objects_list.append(xp_drop)

def reset():
   objects_list.clear()