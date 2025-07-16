from math import sqrt

from PPlay.sprite import *
from PPlay.mouse import *

import pygame
import globals
import states.game as game
import objects

player = {}
item_list = []
VELOCIDADE = 250
last_player_attack = 0

def add_item(item):
    if item == "FIREBALL":
        item_list.append(Sprite("assets/fireball_icon.png"))

def spawn():
    WINDOW = globals.WINDOW

    player["HP"] = 100
    player["ATK"] = 1
    player["ATK-COOLDOWN"] = 2500
    player["RES"] = 1 # Resistance
    player["SPD"] = 1

    player["LEVEL"] = 0
    player["XP"] = 0
    player["XP_MAX"] = 100 # qtd de xp necessária p/a subir de level
    
    player["ENEMIES_KILLED"] = 0

    player["SPRITE"] = Sprite("assets/curupira.png", frames = 3)
    player["SPRITE"].set_total_duration(700)    
    player["SPRITE"].set_position(
        (WINDOW.width-player["SPRITE"].width)//2, 
        (WINDOW.height - player["SPRITE"].height)//2
    )

    # 1: Olhando p/a direita
    # 0: Olhando p/a esquerda
    player["FACING_RIGHT"] = 1

    add_item("FIREBALL")


def input(KEYBOARD, MOUSE):
    global VELOCIDADE, last_player_attack
    delta_t = game.delta_t
    cam_offset = game.cam_offset

    if KEYBOARD.key_pressed("W"):
        cam_offset[1] -= VELOCIDADE * delta_t
        player["SPRITE"].update()
    elif KEYBOARD.key_pressed("S"):
        cam_offset[1] += VELOCIDADE * delta_t
        player["SPRITE"].update()
    
    if KEYBOARD.key_pressed("A"):
        cam_offset[0] -= VELOCIDADE * delta_t
        player["SPRITE"].update()
        player["FACING_RIGHT"] = 0
    elif KEYBOARD.key_pressed("D"):
        cam_offset[0] += VELOCIDADE * delta_t
        player["SPRITE"].update()
        player["FACING_RIGHT"] = 1

    if globals.manual_mode and MOUSE.is_button_pressed(1) and MOUSE.is_on_screen() and player["ATK-COOLDOWN"] < pygame.time.get_ticks() - last_player_attack:
        alvo = MOUSE.get_position()
        player_x = player["SPRITE"].x
        player_y = player["SPRITE"].y
        
        objects.fireball_spawn(player_x + game.cam_offset[0], 
            player_y + game.cam_offset[1], 
            alvo[0] + game.cam_offset[0], 
            alvo[1] + game.cam_offset[1]
        )

        last_player_attack = pygame.time.get_ticks()

def update_info():
    # Checa se já pode subir de level
    if player["XP"] >= player["XP_MAX"]:
        player["LEVEL"] += 1
        player["XP"] = player["XP_MAX"] - player["XP"]
        player["XP_MAX"] *= 2 # Dobra a qtd necessária de xp com cada nível

def reset():
    global last_player_attack
    last_player_attack = 0
    player.clear()

debug_mode = 0

def auto_attack(enemies_list):
    global last_player_attack

    player_x = player["SPRITE"].x
    player_y = player["SPRITE"].y
    centro_player = [player_x + player["SPRITE"].width/2, player_y + player["SPRITE"].height/2]
    
    centro_inimigo_x = None
    centro_inimigo_y = None
    menor_distancia = float('inf')

    if enemies_list != []:
        # Se está em cooldown ainda, não faz nem sentido ter que calcular tudo isso
        if player["ATK-COOLDOWN"] < pygame.time.get_ticks() - last_player_attack:
            for enemy in enemies_list:
                inimigo_x_corrigido = enemy["X"] - game.cam_offset[0]
                inimigo_y_corrigido = enemy["Y"] - game.cam_offset[1]

                centro_inimigo = [inimigo_x_corrigido + enemy["SPRITE"].width/2, inimigo_y_corrigido + enemy["SPRITE"].height/2]
                # Distância de pontos: sqrt((x1-x0)^2 + (y1-y0)^2)
                distancia = sqrt((centro_inimigo[0] - centro_player[0])**2 + (centro_inimigo[1] - centro_player[1])**2)

                if distancia < menor_distancia:
                    menor_distancia = distancia
                    centro_inimigo_x = centro_inimigo[0]
                    centro_inimigo_y = centro_inimigo[1]

            objects.arrow_spawn(player_x + game.cam_offset[0], 
                        player_y + game.cam_offset[1], 
                        centro_inimigo_x + game.cam_offset[0], 
                        centro_inimigo_y + game.cam_offset[1]
                        )
            last_player_attack = pygame.time.get_ticks()

    if debug_mode:
        WINDOW = globals.WINDOW
        pygame.draw.rect(WINDOW.get_screen(), (0,255,0), (centro_player[0]-7, centro_player[1]-7, 14, 14))
        if centro_inimigo_x != None:
            pygame.draw.rect(WINDOW.get_screen(), (0,255,255), (centro_inimigo_x-7, centro_inimigo_y-7, 14, 14))
