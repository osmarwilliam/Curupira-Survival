# TODO LIST:
# 1 - COLISÃO E MORTE DE INIMIGOS
# 1.1 - CONTADOR DE MORTES
# 3 - PLAYER STATS
# 4 - XP DROP

# BUGS CONHECIDOS:
# X

from PPlay.window import *
from PPlay.sprite import *

import states.game as game
from states.menu import mostrar_menu

# game_sys é o dicionário que contém as principais variáveis do programa, como Window, Keyboard, Mouse e Sprites.
game_sys = {}

# SPRITE ITENS AUXILIARES P/A DEPOIS IMPLEMENTAR
# "COMIDA": Sprite("assets/comida.png")
# "RELOGIO": Sprite("assets/relogio.png")
# "BAU": Sprite("assets/bau.png")

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