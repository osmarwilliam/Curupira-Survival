from utils import clicked

menu_bg_color = (22,158,38)

def mostrar_menu(game_sys):
    """
    Mostra o menu do jogo
    Dependências: game_sys["WINDOW"], game_sys["SPRITES"], game_sys["MOUSE"]
    """

    # EXTRAÇÃO DAS DEPENDÊNCIAS DA FUNÇÃO
    WINDOW = game_sys["WINDOW"]
    sprites = game_sys["SPRITES"]    

    WINDOW.set_background_color(menu_bg_color)

    BUTTON_WIDTH = sprites["botao_jogar"].width
    BUTTON_HEIGHT = sprites["botao_jogar"].height

    play_button = sprites["botao_jogar"]
    play_button.set_position((WINDOW.width - BUTTON_WIDTH)/2, WINDOW.height/2 - BUTTON_HEIGHT - 20/2)
    
    exit_button = sprites["botao_sair"]
    exit_button.set_position( (WINDOW.width - BUTTON_WIDTH)/2, WINDOW.height/2 + 20/2)

    play_button.draw()
    exit_button.draw()
        
    WINDOW.update()

    if clicked(game_sys["MOUSE"], play_button):
        game_sys["STATE_SWITCHER"] = "GAME"
    elif clicked(game_sys["MOUSE"], exit_button):
        WINDOW.close()
