from PPlay.window import *

import config
import states.jogo as jogo

def init():
    config.janela = Window(1000,800)
    config.janela.set_title("Curupira Survival")

    # TECLADO
    config.teclado = config.janela.get_keyboard()

init()

config.CONTROLADOR = config.JOGO

# LOOP PRINCIPAL
while True:
    match (config.CONTROLADOR):
        case config.JOGO:
            jogo.comecar_jogo()