import random

from player import player
from PPlay.sprite import *

enemies_list = []

def spawn(type):
    new_enemy = {
        "TYPE": type.upper(),
        "X": random.randint(0, 800), 
        "Y": random.randint(0, 800),
        "ATK-COOLDOWN": 500, # Por enquanto é o mesmo cooldown para todos os inimigos
        "LAST-ATK": 0
    }
    
    if new_enemy["TYPE"] == "JAVALI":
        new_enemy["HP"] = 150
        new_enemy["ATK"] = 10
        new_enemy["SPEED"] = 150
        new_enemy["SPRITE"] = Sprite("assets/javali.png", frames = 2)
        new_enemy["CHARGED"] = False
    elif new_enemy["TYPE"] == "LENHADOR":
        new_enemy["HP"] = 100
        new_enemy["ATK"] = 5
        new_enemy["SPEED"] = 100
        new_enemy["SPRITE"] = Sprite("assets/lenhador.png")
    elif new_enemy["TYPE"] == "CACADOR":
        new_enemy["HP"] = 100
        new_enemy["SPRITE"] = Sprite("assets/cacador.png")
    
    enemies_list.append(new_enemy)

def lenhador_ai(enemy, player_x, player_y, delta_t):
    dir_x = player_x - enemy["X"]
    dir_y = player_y - enemy["Y"]

    distancia = (dir_x**2 + dir_y**2)**0.5 # Teorema de Pitágoras

    if distancia > 0: # Evita divisão por 0
        dir_x /= distancia
        dir_y /= distancia

    enemy["X"] += dir_x * enemy["SPEED"] * delta_t
    enemy["Y"] += dir_y * enemy["SPEED"] * delta_t

def javali_ai(enemy, player_x, player_y, delta_t):
    """ 
    =====| Função da IA do Javali |=====
    Inputs:
        player_x = player["SPRITE"].x + cam_offset[0]
        player_y = player["SPRITE"].y + cam_offset[1]
    """
    dir_x = player_x - enemy["X"]
    dir_y = player_y - enemy["Y"]

    distancia = (dir_x**2 + dir_y**2)**0.5 # Teorema de Pitágoras

    if distancia > 0: # Evita divisão por 0
        dir_x /= distancia
        dir_y /= distancia

    if int(distancia) <= 300:
        print("CHARGE")
        enemy["SPEED"] = 300

        if not enemy["CHARGED"]:
            enemy["X"] += dir_x * enemy["SPEED"] * delta_t
            enemy["Y"] += dir_y * enemy["SPEED"] * delta_t
            enemy["CHARGED"] = True
        else:
            enemy["X"] += enemy["SPEED"] * delta_t
            enemy["Y"] += enemy["SPEED"] * delta_t
    else:
        enemy["X"] += dir_x * enemy["SPEED"] * delta_t
        enemy["Y"] += dir_y * enemy["SPEED"] * delta_t

def think(cam_offset, delta_t):
    """
    Aqui é definido o comportamento da IA de cada inimigo
    """
    player_x = player["SPRITE"].x + cam_offset[0]
    player_y = player["SPRITE"].y + cam_offset[1]

    for enemy in enemies_list:
        if enemy["TYPE"] == "JAVALI":
            javali_ai(enemy, player_x, player_y, delta_t)
        if enemy["TYPE"] == "LENHADOR":
            lenhador_ai(enemy, player_x, player_y, delta_t)