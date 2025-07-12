from PPlay.sprite import *
from PPlay.collision import Collision
from PPlay.sound import *

import random

from ui import desenhar_ui
import utils
import player
import enemies
import objects
import waves


cam_offset = [0,0]

start_time = None  
delta_t = None

# Efeitos sonoros
hitSound = Sound("assets/audio/hit.wav")
xpSound = Sound("assets/audio/xp.wav")

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
            object["X"] += object["DIR_X"] * object["SPEED"] * delta_t
            object["Y"] += object["DIR_Y"] * object["SPEED"] * delta_t

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

    for enemy in enemies.enemies_list: # TODO: Ajeitar inversão do sprite
        enemy["SPRITE"].set_position(enemy["X"] - cam_offset[0], enemy["Y"] - cam_offset[1])
        #enemy["SPRITE_L"].set_position(enemy["X"] - cam_offset[0], enemy["Y"] - cam_offset[1]) 

        if enemy["TYPE"] == "LENHADOR":
            #if enemy["SPRITE_R"].x > player.player["SPRITE"].x:
            #    enemy["SPRITE_L"].update()
            #    enemy["SPRITE_L"].draw()
            #else:
            enemy["SPRITE"].update()
            enemy["SPRITE"].draw()

def collision_detection():
    """
    Detecta se houve alguma colisão no jogo
    """
    global hitSound
    # TODO: otimizar a detecção de colisão igual o do space invaders
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
                xpSound.play()
                objects.objects_list.remove(object)
    
    for enemy in enemies.enemies_list:
        verificavel = True
        if enemy["SPRITE"].x > player.player["SPRITE"].x + player.player["SPRITE"].width:
            verificavel = False
        elif enemy["SPRITE"].x + enemy["SPRITE"].width < player.player["SPRITE"].x:
            verificavel = False
        elif enemy["SPRITE"].y + enemy["SPRITE"].height < player.player["SPRITE"].y:
            verificavel = False
        elif enemy["SPRITE"].y > player.player["SPRITE"].y + player.player["SPRITE"].height:
            verificavel = False

        if verificavel and pygame.time.get_ticks() - enemy["LAST-ATK"] > enemy["ATK-COOLDOWN"]:
            if enemy["SPRITE"].collided_perfect(player.player["SPRITE"]):
                player.player["HP"] -= enemy["ATK"]
                hitSound.play()
                enemy["LAST-ATK"] = pygame.time.get_ticks()

def player_input(KEYBOARD):
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

def run(game_sys):
    global start_time, delta_t
    start_time = pygame.time.get_ticks()
    
    # P/a o código ficar menos verboso e evitar erros de digitação
    WINDOW = game_sys["WINDOW"]
    KEYBOARD = game_sys["KEYBOARD"]

    player.spawn(WINDOW)
    
    cam_offset[0] = player.player["SPRITE"].x - WINDOW.width // 2
    cam_offset[1] = player.player["SPRITE"].y - WINDOW.height // 2
    
    backgroundMusic = Sound("assets/audio/bg1_the-gensokyo-the-gods-loved.mp3")
    backgroundMusic.loop = True
    backgroundMusic.play()

    while True:
        delta_t = WINDOW.delta_time()

        # TODO: FAZER A MÚSICA DE FUNDO PAUSAR QUANDO APERTAR O BOTÃO DO MENU
        if KEYBOARD.key_pressed("ESC"):
            game_sys["STATE_SWITCHER"] = "MENU"
            return 0

        player_input(KEYBOARD)

        utils.draw_background(WINDOW, cam_offset)
        
        waves.auto_wave(WINDOW)
        collision_detection()
        update_scenario()
        draw_scenario()

        if player.player["HP"] <= 0:
            backgroundMusic.stop()
            Sound("assets/audio/game-over.wav").play()
            utils.reset_game()
            game_sys["STATE_SWITCHER"] = "GAME_OVER"
            return 0

        player.update_info()
        player.draw() 

        if enemies.enemies_list != []:
            player.auto_attack(WINDOW, enemies.enemies_list)
            enemies.think(cam_offset, delta_t)

        desenhar_ui(WINDOW, player.player)
        #utils.draw_version(WINDOW)
        #WINDOW.clear()
        WINDOW.update()
        