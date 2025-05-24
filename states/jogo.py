# TODO LIST:
# TORNAR MAIS LEGÍVEL SE POSSÍVEL
# 2 - COLISÃO E MORTE DE INIMIGOS
# 2.1 - CONTADOR DE MORTES
# 3 - PLAYER STATS
# 4 - XP DROP

# TODO: ARRUMAR CAMERA OFFSET QUE QUEBROU O JOGO

from PPlay.sprite import *

import random

from ui import desenhar_ui
import player
import enemies
import objects

cam_offset = [0,0]

start_time = None  

def update_scenario(delta_t): 
    # ATUALIZA AS COORDENADAS REAIS DO CENÁRIO
    # Obs.: coordenadas reais de objetos estáticos não são atualizadas
     
    for object in objects.objects_list:
        if object["TYPE"] == "bullet":
            dir_x = object["TARGET_X"] - object["X"]
            dir_y = object["TARGET_Y"] - object["Y"]

            distancia = (dir_x**2 + dir_y**2)**0.5 # Teorema de Pitágoras

            if distancia > 0: # Evita divisão por 0
                dir_x /= distancia
                dir_y /= distancia

            # TODO: arrumar com o offset da camera
            object["X"] += dir_x * 400 * delta_t # 400 -> velocidade
            object["Y"] += dir_y * 400 * delta_t

def draw_scenario(): # DESENHA OS SPRITES NAS COORDENADAS CORRIGIDAS COM O OFFSET
    x = 0
    y = 1

    for object in objects.objects_list:
        object["SPRITE"].set_position(object["X"] - cam_offset[x], object["Y"] - cam_offset[y])
        object["SPRITE"].draw()

    for enemy in enemies.enemies_list:
        enemy["SPRITE"].set_position(enemy["X"] - cam_offset[x], enemy["Y"] - cam_offset[y])
        enemy["SPRITE"].draw()

def comecar_jogo(sys_state):
    global start_time
    start_time = pygame.time.get_ticks()

    WINDOW = sys_state["WINDOW"]
    KEYBOARD = sys_state["KEYBOARD"]

    player.spawn(WINDOW)

    cam_offset[0] = player.player["SPRITE"].x - WINDOW.width // 2
    cam_offset[1] = player.player["SPRITE"].y - WINDOW.height // 2

    for _ in range(3): 
        enemies.spawn(sys_state["SPRITES"], random.choice(["JAVALI", "LENHADOR", "CACADOR"]))
    
    while True:
        delta_t = WINDOW.delta_time()


        # LÓGICA
        if (KEYBOARD.key_pressed("ESC")):
            sys_state["controlador"] = "MENU"
            return 0

        if KEYBOARD.key_pressed("W"):
            cam_offset[1] -= player.VELOCIDADE * delta_t
        elif KEYBOARD.key_pressed("S"):
            cam_offset[1] += player.VELOCIDADE * delta_t

        if KEYBOARD.key_pressed("A"):
            cam_offset[0] -= player.VELOCIDADE * delta_t
            player.change_side("LEFT")
        elif KEYBOARD.key_pressed("D"):
            cam_offset[0] += player.VELOCIDADE * delta_t
            player.change_side("RIGHT")
        
        WINDOW.set_background_color([28,93,42])

        update_scenario(delta_t)
        draw_scenario()
        
        player.draw() 
        player.auto_attack(WINDOW, sys_state["SPRITES"], enemies.enemies_list)

        desenhar_ui(WINDOW, player.player)
        WINDOW.update()

        #TODO: MOVIMENTAÇÃO DA IA
        #enemies.think()
