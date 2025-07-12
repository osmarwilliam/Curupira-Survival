from utils import clicked

from PPlay.sprite import *

menu_bg_color = (22,158,38)

def mostrar_menu(game_sys):
    WINDOW = game_sys["WINDOW"]

    WINDOW.set_background_color(menu_bg_color)

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
        
    WINDOW.update()

    if clicked(game_sys["MOUSE"], play_button):
        game_sys["STATE_SWITCHER"] = "GAME"
    elif clicked(game_sys["MOUSE"], config_button):
        game_sys["STATE_SWITCHER"] = "CONFIG"
    elif clicked(game_sys["MOUSE"], exit_button):
        WINDOW.close()
