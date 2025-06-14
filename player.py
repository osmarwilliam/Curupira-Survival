from math import sqrt

from PPlay.sprite import *

import pygame

import states.game as game
import objects

player = {}
VELOCIDADE = 500
last_player_attack = 0

def spawn(janela):
    player["HP"] = 100
    player["XP"] = 0
    player["LEVEL"] = 0
    player["ENEMIES_KILLED"] = 0

    player["ATK-COOLDOWN"] = 2500

    player["SPRITE"] = Sprite("assets/curupira.png", frames = 2)
    player["SPRITE"].set_loop(0)
    player["SPRITE"].set_total_duration(0)
    
    player["SPRITE"].set_position(
        (janela.width-player["SPRITE"].width)//2, 
        (janela.height - player["SPRITE"].height)//2
    )

def draw():
    player["SPRITE"].draw()

def change_side(side):
    if side == "LEFT":
        player["SPRITE"].set_curr_frame(1)
    elif side == "RIGHT":
        player["SPRITE"].set_curr_frame(0)

debug_mode = 1

def arrow_spawn(x, y, target_x, target_y):
    new_arrow = {
        "TYPE": "ARROW",
        "SPEED": 400,
        "X": x,
        "Y": y,
        "TARGET_X": target_x,
        "TARGET_Y": target_y,
        "SPRITE": Sprite("assets/flecha.png")
    }
    
    objects.objects_list.append(new_arrow)

def auto_attack(janela, enemies_list):
    global last_player_attack

    player_x = player["SPRITE"].x
    player_y = player["SPRITE"].y
    centro_player = [player_x + player["SPRITE"].width/2, player_y + player["SPRITE"].height/2]
    
    inimigo_mais_proximo = None
    centro_inimigo_x = None
    centro_inimigo_y = None
    menor_distancia = float('inf')

    # Se ainda está em atk cooldown, nem faz sentido calcular isso aqui
    for enemy in enemies_list:
        inimigo_x_corrigido = enemy["X"] - game.cam_offset[0]
        inimigo_y_corrigido = enemy["Y"] - game.cam_offset[1]

        centro_inimigo = [inimigo_x_corrigido + enemy["SPRITE"].width/2, inimigo_y_corrigido + enemy["SPRITE"].height/2]
        # Distância de pontos: sqrt((x1-x0)^2 + (y1-y0)^2)
        distancia = sqrt((centro_inimigo[0] - centro_player[0])**2 + (centro_inimigo[1] - centro_player[1])**2)

        if distancia < menor_distancia:
            menor_distancia = distancia
            inimigo_mais_proximo = enemy
            centro_inimigo_x = centro_inimigo[0]
            centro_inimigo_y = centro_inimigo[1]

    # Auto Attack
    if player["ATK-COOLDOWN"] < pygame.time.get_ticks() - last_player_attack:
        arrow_spawn(player_x + game.cam_offset[0], 
                    player_y + game.cam_offset[1], 
                    centro_inimigo_x + game.cam_offset[0], 
                    centro_inimigo_y + game.cam_offset[1]
                    )
        last_player_attack = pygame.time.get_ticks()

    if debug_mode:
        pygame.draw.rect(janela.get_screen(), (0,255,0), (centro_player[0]-7, centro_player[1]-7, 14, 14))
        pygame.draw.rect(janela.get_screen(), (0,255,255), (centro_inimigo_x-7, centro_inimigo_y-7, 14, 14))
