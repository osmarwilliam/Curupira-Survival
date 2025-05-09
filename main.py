from PPlay.window import *

import config
import states.jogo as jogo
import states.menu as menu

def init():
    config.janela = Window(1000,800)
    config.janela.set_title("Curupira Survival")

    # TECLADO
    config.teclado = config.janela.get_keyboard()

    # MOUSE
    config.mouse = config.janela.get_mouse()

init()

config.CONTROLADOR = config.MENU

# LOOP PRINCIPAL
while True:
    match (config.CONTROLADOR):
        case config.JOGO:
            jogo.comecar_jogo()
        case config.MENU:
            menu.mostrar_menu(1)