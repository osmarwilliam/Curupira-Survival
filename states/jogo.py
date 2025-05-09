import config

def comecar_jogo():
    while True:
        # VISUAL
        config.janela.set_background_color([0,25,0])

        config.janela.update()

        # LÓGICA

        if (config.teclado.key_pressed("ESC")):
            config.janela.close()

