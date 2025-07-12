import globals
from utils import clicked
from PPlay.sprite import *

MENU_BG_COLOR = (22,158,38)

def mostrar_menu():
    WINDOW = globals.WINDOW
    MOUSE = globals.MOUSE

    WINDOW.set_background_color(MENU_BG_COLOR)

    BUTTON_WIDTH = Sprite("assets/botao-jogar.png").width
    BUTTON_HEIGHT = Sprite("assets/botao-jogar.png").height
    MEIO = (WINDOW.height - BUTTON_HEIGHT)/2
    PADDING = 20

    play_button = Sprite("assets/botao-jogar.png")
    play_button.set_position((WINDOW.width - BUTTON_WIDTH)/2, MEIO - BUTTON_HEIGHT - PADDING)
    play_button.draw()    

    config_button = Sprite("assets/botao-configuracoes.png")
    config_button.set_position((WINDOW.width - BUTTON_WIDTH)/2, MEIO)
    config_button.draw()

    exit_button = Sprite("assets/botao-sair.png")
    exit_button.set_position( (WINDOW.width - BUTTON_WIDTH)/2, MEIO + BUTTON_HEIGHT + PADDING)
    exit_button.draw()
        
    if clicked(MOUSE, play_button):
        globals.current_state = "GAME"
    elif clicked(MOUSE, config_button):
        globals.current_state = "CONFIG"
    elif clicked(MOUSE, exit_button):
        WINDOW.close()
