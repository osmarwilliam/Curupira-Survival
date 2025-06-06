from PPlay.sprite import *
from PPlay.collision import Collision

import random

from ui import desenhar_ui
import player
import enemies
import objects

cam_offset = [0,0]

start_time = None  
delta_t = None

def update_scenario(): 
    """
    Atualiza as coordenadas reais de cada objeto e inimigo no cenário
    Obs. 1: Coordenada real -> A coordenada de fato do objeto
            Coordenada corrigida com offset -> A coordenada de onde o objeto está na tela corrigido com o offset da câmera

    Obs. 2: Coordenadas reais de objetos estáticos não são atualizadas pois eles não se movimentam
    
    Args: 
        delta_t: delta time da janela
    """
    global delta_t

    for object in objects.objects_list:
        if object["TYPE"] == "ARROW":
            dir_x = object["TARGET_X"] - object["X"]
            dir_y = object["TARGET_Y"] - object["Y"]

            distancia = (dir_x**2 + dir_y**2)**0.5 # Teorema de Pitágoras

            if distancia > 0: # Evita divisão por 0
                dir_x /= distancia
                dir_y /= distancia

            object["X"] += dir_x * object["SPEED"] * delta_t
            object["Y"] += dir_y * object["SPEED"] * delta_t

def draw_scenario(): 
    """ 
    Desenha os sprites nas coordenadas corrigidas com o offset
    Obs.: Coordenada corrigida com offset -> A coordenada de onde o objeto está na tela corrigido com o offset da câmera
    """

    for object in objects.objects_list:
        object["SPRITE"].set_position(object["X"] - cam_offset[0], object["Y"] - cam_offset[1])
        object["SPRITE"].draw()

        if object["TYPE"] == "XP":
            object["SPRITE"].update()

    for enemy in enemies.enemies_list:
        enemy["SPRITE"].set_position(enemy["X"] - cam_offset[0], enemy["Y"] - cam_offset[1])
        enemy["SPRITE"].draw()

def collision_detection():
    """
    Detecta se houve alguma colisão no jogo
    """
    for object in objects.objects_list:
        if object["TYPE"] == "ARROW":
            for enemy in enemies.enemies_list:
                if object["SPRITE"].collided_perfect(enemy["SPRITE"]):
                    objects.drop_xp(enemy)
                    objects.objects_list.remove(object)
                    enemies.enemies_list.remove(enemy)
                    player.player["ENEMIES_KILLED"] += 1
                    break
        elif object["TYPE"] == "XP":
            if object["SPRITE"].collided(player.player["SPRITE"]):
                player.player["XP"] += object["VALUE"]
                objects.objects_list.remove(object)

def run(game_sys):
    global start_time, delta_t
    start_time = pygame.time.get_ticks()
    
    # P/a o código ficar menos verboso e evitar erros de digitação
    WINDOW = game_sys["WINDOW"]
    KEYBOARD = game_sys["KEYBOARD"]

    player.spawn(WINDOW)
    
    cam_offset[0] = player.player["SPRITE"].x - WINDOW.width // 2
    cam_offset[1] = player.player["SPRITE"].y - WINDOW.height // 2

    for _ in range(3): 
        enemies.spawn(random.choice(["JAVALI", "LENHADOR", "CACADOR"]))

    while True:
        delta_t = WINDOW.delta_time()

        if KEYBOARD.key_pressed("ESC"):
            game_sys["STATE_SWITCHER"] = "MENU"
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
        
        collision_detection()
        update_scenario()
        draw_scenario()

        player.draw() 

        if enemies.enemies_list != []:
            player.auto_attack(WINDOW, enemies.enemies_list)
            enemies.think(cam_offset, delta_t)

        desenhar_ui(WINDOW, player.player)
        WINDOW.update()