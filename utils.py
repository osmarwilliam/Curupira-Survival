def clicou(mouse, botao):
    return mouse.is_button_pressed(1) and mouse.is_over_object(botao)
