from PPlay.sprite import *

import random

import config

def comecar_jogo():
    player = Sprite("assets/curupira.png", frames = 2)
    player.set_loop(0)
    player.set_total_duration(0)
    player.set_position(config.janela.width/2, config.janela.height/2)

    javali = Sprite("assets/javali.png", frames = 2)
    javali.set_loop(0)
    javali.set_total_duration(0)
    javali.set_position(random.randint(0,config.janela.width), random.randint(0,config.janela.height))

    vel_jogador = 500
    vel_javali = 150

    while True:
        delta_t = config.janela.delta_time()

        # VISUAL
        config.janela.set_background_color([0,25,0])
        
        player.draw()
        javali.draw()
        config.janela.update()

        # LÓGICA
        if (config.teclado.key_pressed("ESC")):
            config.janela.close()

        if config.teclado.key_pressed("W"):
            player.y -= vel_jogador * delta_t
        elif config.teclado.key_pressed("S"):
            player.y += vel_jogador * delta_t

        if config.teclado.key_pressed("A"):
            player.x -= vel_jogador * delta_t
            player.set_curr_frame(1)
        elif config.teclado.key_pressed("D"):
            player.x += vel_jogador * delta_t
            player.set_curr_frame(0)

        # MOVIMENTAÇÃO IA (SERÁ TUDO SUBSTITUIDO POR UM OFFSET)
        #if javali.x > player.x:
        #    javali.x -= vel_javali * delta_t
        #    javali.set_curr_frame(1)
        #else:
        #    javali.x += vel_javali * delta_t
        #    javali.set_curr_frame(0)
        
        #if javali.y > player.y:
        #    javali.y -= vel_javali * delta_t
        #elif javali.y < player.y:
        #    javali.y += vel_javali * delta_t