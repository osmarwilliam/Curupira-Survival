import random

from player import player
from PPlay.sprite import *

enemies_list = []

def spawn(type):
    new_enemy = {
        "TYPE": type.upper(),
        "X": random.randint(0, 800), 
        "Y": random.randint(0, 800),
    }
    
    if new_enemy["TYPE"] == "JAVALI":
        new_enemy["HP"] = 150
        new_enemy["SPRITE"] = Sprite("assets/javali.png", frames = 2)
    elif new_enemy["TYPE"] == "LENHADOR":
        new_enemy["HP"] = 100
        new_enemy["SPEED"] = 100
        new_enemy["SPRITE"] = Sprite("assets/lenhador.png")
    elif new_enemy["TYPE"] == "CACADOR":
        new_enemy["HP"] = 100
        new_enemy["SPRITE"] = Sprite("assets/cacador.png")
    
    enemies_list.append(new_enemy)

def think(cam_offset, delta_t):
    """
    Aqui é definido o comportamento da IA de cada inimigo
    """

    player_x = player["SPRITE"].x + cam_offset[0]
    player_y = player["SPRITE"].y + cam_offset[1]

    for enemy in enemies_list:
        if enemy["TYPE"] == "LENHADOR":
            # Depois fazer o centro certinho dos sprites
            dir_x = player_x - enemy["X"]
            dir_y = player_y - enemy["Y"]

            distancia = (dir_x**2 + dir_y**2)**0.5 # Teorema de Pitágoras

            if distancia > 0: # Evita divisão por 0
                dir_x /= distancia
                dir_y /= distancia

            enemy["X"] += dir_x * enemy["SPEED"] * delta_t
            enemy["Y"] += dir_y * enemy["SPEED"] * delta_t