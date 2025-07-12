from PPlay.gameimage import *
from PPlay.sprite import *

import states.menu as menu
import states.game as game
from utils import clicked

def mostrar_configs(game_sys):
    WINDOW = game_sys["WINDOW"]

    WINDOW.set_background_color(menu.menu_bg_color)

    manualButton = GameImage("assets/botao-modo-manual.png")
    manualButton.set_position( 100, 100)
    manualButton.draw()

    # TODO: Ajustar a posição disso aq
    manualButtonPress = Sprite("assets/press-button.png", frames=2)
    manualButtonPress.set_curr_frame(game.manual_mode)
    manualButtonPress.set_position(100 + manualButton.width + 40, 100)
    manualButtonPress.draw()

    returnButton = GameImage("assets/botao-voltar.png")
    returnButton.set_position((WINDOW.width - returnButton.width)/2, WINDOW.height - 150)
    returnButton.draw()

    WINDOW.update()

    if game_sys["KEYBOARD"].key_pressed("ESC") or clicked(game_sys["MOUSE"], returnButton): 
        game_sys["STATE_SWITCHER"] = "MENU"

    if clicked(game_sys["MOUSE"], manualButtonPress): 
        game.manual_mode = 1 - game.manual_mode # inverte