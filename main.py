from PPlay.window import *
from PPlay.sprite import *

import states.jogo as jogo
import states.menu as menu

sys_state = {}

def load_sprites():
    sprites = {
        # SPRITE BOTÕES
        "botao_jogar": Sprite("assets/botao-jogar.png"),
        "botao_sair": Sprite("assets/botao-sair.png"),

        # SPRITE MONSTROS
        "JAVALI": Sprite("assets/javali.png", frames = 2),
        "LENHADOR": Sprite("assets/lenhador.png"),
        "CACADOR": Sprite("assets/cacador.png"),

        # SPRITE ITENS AUXILIARES
        "COMIDA": Sprite("assets/comida.png"),
        "RELOGIO": Sprite("assets/relogio.png"),
        "BAU": Sprite("assets/bau.png"),

        "FLECHA": Sprite("assets/flecha.png")
    }

    return sprites

def init():
    sys_state["WINDOW"] = Window(1000,800)
    sys_state["WINDOW"].set_title("Curupira Survival")

    sys_state["KEYBOARD"] = sys_state["WINDOW"].get_keyboard()
    sys_state["MOUSE"] = sys_state["WINDOW"].get_mouse()

    sys_state["controlador"] = "MENU" # Inicia o jogo pelo menu

    sys_state["SPRITES"] = load_sprites()

init()

while True:
    if sys_state["controlador"] == "JOGO":
        jogo.comecar_jogo(sys_state)
    elif sys_state["controlador"] == "MENU":
        menu.mostrar_menu(sys_state)
