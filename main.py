# TODO LIST:
# 1 - modificar no 'ui' o xp_max conforme o nível do jogador, talvez mudar para o módulo do player
# 2 - PLAYER STATS

# BUGS CONHECIDOS:
# - bug na colisão da flecha com o caçador especificamente

from PPlay.window import *
from PPlay.sprite import *

import states.game as game
from states.menu import mostrar_menu

# game_sys é o dicionário que contém as principais variáveis do programa, como Window, Keyboard, Mouse e Sprites.
game_sys = {}

def init():
    """
    Inicializa as principais variáveis do programa e as armazena no game_sys
    """
    game_sys["WINDOW"] = Window(1000,800)
    game_sys["WINDOW"].set_title("Curupira Survival")

    game_sys["KEYBOARD"] = game_sys["WINDOW"].get_keyboard()
    game_sys["MOUSE"] = game_sys["WINDOW"].get_mouse()

    game_sys["STATE_SWITCHER"] = "MENU"

init()

while True:
    if game_sys["STATE_SWITCHER"] == "GAME":
        game.run(game_sys)
    elif game_sys["STATE_SWITCHER"] == "MENU":
        mostrar_menu(game_sys)