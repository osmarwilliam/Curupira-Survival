from PPlay.sprite import *

import random

import config

lista_objetos = []

VEL_JOGADOR = 500

def objeto_spawn():
    novo_objeto = {
        "x": 100, 
        "y": 100,
    }

    lista_objetos.append(novo_objeto)

def atualizar_objeto(objeto, movimento_jogador_x, movimento_jogador_y, delta_t):
     objeto["x"] += movimento_jogador_x * VEL_JOGADOR * delta_t
     objeto["y"] += movimento_jogador_y * VEL_JOGADOR * delta_t

def desenhar_objeto(objeto):
    objeto_visual = Sprite("assets/javali.png", frames = 2)
    objeto_visual.set_position(objeto["x"], objeto["y"])
    objeto_visual.draw()

def comecar_jogo():
    player = Sprite("assets/curupira.png", frames = 2)
    player.set_loop(0)
    player.set_total_duration(0)
    player.set_position((config.janela.width-player.width)/2, (config.janela.height - player.height)/2)

    objeto_spawn()
    vel_javali = 150

    while True:
        delta_t = config.janela.delta_time()

        # LÓGICA
        if (config.teclado.key_pressed("ESC")):
            config.CONTROLADOR = config.MENU
            return 0

        movimento_jogador_x = 0
        movimento_jogador_y = 0

        if config.teclado.key_pressed("W"):
            movimento_jogador_y = 1
        elif config.teclado.key_pressed("S"):
            movimento_jogador_y = -1

        if config.teclado.key_pressed("A"):
            movimento_jogador_x = 1
            player.set_curr_frame(1)
        elif config.teclado.key_pressed("D"):
            movimento_jogador_x = -1
            player.set_curr_frame(0)

        config.janela.set_background_color([28,93,42])

        for objeto in lista_objetos:
            print(objeto["x"])
            print(objeto["y"])
            atualizar_objeto(objeto, movimento_jogador_x, movimento_jogador_y, delta_t)
            desenhar_objeto(objeto)
        
        player.draw()
        config.janela.update()


        #TODO: MOVIMENTAÇÃO DA IA