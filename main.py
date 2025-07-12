# TODO LIST:
# IMPLEMENTAR ITENS
# 0.2 - Arrumar bug da flecha - fazer ela seguir linearmente
# 0.3 - Remover projéteis que saem muito da tela
# 1 - PLAYER STATS
# 3 - Uma opção nas configurações para alterar entre mira/ataque automático ou manual=
# TODO: otimizar a detecção de colisão de projéteis igual o do space invaders
# TODO: Inimigos não ficar o sprite um em cima do outro
# BUGS CONHECIDOS:
# - inimigos spawnando na tua frente, eles spawnam em coordenadas fixas, ajuste para coordenadas a partir do 
# player
# TODO: ARRANJAR UM METODO DO SPRITE VIRAR DE ACORDO COM A DIREÇÃO DO INIMIGO
# TODO: ADICIONAR EFEITO SONORO DE QUANDO JOGADOR COLETA ITEM AUXILIAR
# TODO: FAZER A MÚSICA DE FUNDO PAUSAR QUANDO APERTAR O BOTÃO DO MENU
# TODO: Colisão entre sprites tá muito bugada, parece até que o collided perfect não tá funcionando
# TODO: FAZER ANIMAÇÃO DO CAÇADOR AJOELHANDO E MIRANDO PARA ATIRAR
# TODO: FAZER ANIMAÇÃO DE CHARGE DO JAVALI

from PPlay.window import *
from PPlay.sprite import *

import states.game as game
from states.menu import mostrar_menu
from states.game_over import game_over

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
    elif game_sys["STATE_SWITCHER"] == "GAME_OVER":
        game_over(game_sys)