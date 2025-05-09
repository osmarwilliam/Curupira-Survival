from PPlay.sprite import *

import config

def debug():
    barra_central = Sprite("assets/barra.png", frames = 1)
    barra_central.set_position((config.janela.width - barra_central.width)/2, (config.janela.height-barra_central.height)/2)
    barra_central.draw()

def mostrar_menu(debug_mode):
    while True:
        #VISUAL
        config.janela.set_background_color([22,158,38])

        if debug_mode: 
            debug()
        
        botao_jogar = Sprite("assets/botao-jogar.png", frames = 1)
        
        tamanho_x_botao = botao_jogar.width
        tamanho_y_botao = botao_jogar.height
        
        botao_jogar.set_position((config.janela.width - tamanho_x_botao)/2, config.janela.height/2 - tamanho_y_botao - 20/2)
        botao_sair = Sprite("assets/botao-sair.png", frames = 1)
        botao_sair.set_position( (config.janela.width - tamanho_x_botao)/2, config.janela.height/2 + 20/2)


        botao_jogar.draw()
        botao_sair.draw()
        
        config.janela.update()

        #LÓGICO
        if config.mouse.is_button_pressed(1) and config.mouse.is_over_object(botao_jogar):
            config.CONTROLADOR = config.JOGO
            return 0
        elif config.mouse.is_button_pressed(1) and config.mouse.is_over_object(botao_sair):
            config.janela.close()