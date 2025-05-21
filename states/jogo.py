from PPlay.sprite import *

import random

import config
import ui
import player

lista_objetos = []

start_time = None

def objeto_spawn(tipo):
    novo_objeto = {
        "tipo": tipo.upper(),
        "x": random.randint(0,config.janela.width-50), 
        "y": random.randint(0,config.janela.height-50),
    }
    
    match novo_objeto["tipo"]:
        case "JAVALI":
            novo_objeto["HP"] = 150
        case "LENHADOR":
            novo_objeto["HP"] = 100
        case "CACADOR":
            novo_objeto["HP"] = 100

    lista_objetos.append(novo_objeto)

def atualizar_objetos(movimento_jogador_x, movimento_jogador_y, delta_t):
     for objeto in lista_objetos:
        objeto["x"] += movimento_jogador_x * player.VELOCIDADE * delta_t
        objeto["y"] += movimento_jogador_y * player.VELOCIDADE * delta_t

def desenhar_objetos():
    for objeto in lista_objetos:
        # Depois para melhor eficiência de memória fazer sprite sharing
        match objeto["tipo"]:
            case "JAVALI":
                objeto_visual = Sprite("assets/javali.png", frames = 2)
            case "LENHADOR":
                objeto_visual = Sprite("assets/lenhador.png")
            case "CACADOR":
                objeto_visual = Sprite("assets/cacador.png")
            case "BAU":
                objeto_visual = Sprite("assets/bau.png")
            case "COMIDA":
                objeto_visual = Sprite("assets/comida.png")
            case "RELOGIO":
                objeto_visual = Sprite("assets/relogio.png")

        objeto_visual.set_position(objeto["x"], objeto["y"])
        objeto_visual.draw()

def comecar_jogo():
    player.spawn()

    objeto_spawn("JAVALI")
    objeto_spawn("LENHADOR")
    objeto_spawn("CACADOR")

    objeto_spawn("BAU")
    objeto_spawn("COMIDA")
    objeto_spawn("RELOGIO")

    global start_time
    start_time = pygame.time.get_ticks()

    while True:
        delta_t = config.janela.delta_time()

        # LÓGICA
        if (config.teclado.key_pressed("ESC")):
            config.CONTROLADOR = config.MENU
            return 0

        movimento_jogador_x = 0
        movimento_jogador_y = 0

        if config.teclado.key_pressed("W"):
            movimento_jogador_y = 1
        elif config.teclado.key_pressed("S"):
            movimento_jogador_y = -1

        if config.teclado.key_pressed("A"):
            movimento_jogador_x = 1
            player.change_side("LEFT")
        elif config.teclado.key_pressed("D"):
            movimento_jogador_x = -1
            player.change_side("RIGHT")

        config.janela.set_background_color([28,93,42])

        atualizar_objetos(movimento_jogador_x, movimento_jogador_y, delta_t)
        desenhar_objetos()
        
        player.draw()

        ui.barra_xp()
        config.janela.update()


        #TODO: MOVIMENTAÇÃO DA IA