import pygame
from PPlay.sprite import *

import config
import states.jogo as jogo
import player

WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (88,97,98)
RED = (173, 24, 24)

FONTE = 'Tahoma'

# "segunda camda" da UI, logo embaixo da barra de XP
y_ui = 60  # 60 = barra_xp_height + 10 de padding
 
def mostrar_cronometro(): # Mostra na tela há quanto tempo o jogador iniciou a partida
    tempo_atual = pygame.time.get_ticks() - jogo.start_time
    segundos_decorridos = tempo_atual // 1000 # Converte em segundos

    # Formata o tempo (MM:SS)
    minutos = segundos_decorridos // 60
    segundos = segundos_decorridos % 60
    cronometro = f"{minutos:02d}:{segundos:02d}"

    # Renderiza o texto
    text_surface = pygame.font.SysFont(FONTE, 40).render(cronometro, True, WHITE)
    text_rect = text_surface.get_rect() # Vê o tamanho do texto renderizado
    text_rect.centerx = config.janela.width //2 # Posição X

    # Desenha na tela o texto
    config.janela.draw_text(cronometro, text_rect.x, y_ui, size = 40, color = WHITE, font_name = FONTE, bold = True, italic = False)

def mostrar_itens(): # Desenha os "contâiners" dos itens
    # Código temporário
    pygame.draw.rect(config.janela.get_screen(), BLACK, (10, y_ui, 30*5 + 5*6, 30*2 + 5*3))
    
    pygame.draw.rect(config.janela.get_screen(), GRAY, (15, y_ui+5, 30, 30))
    pygame.draw.rect(config.janela.get_screen(), GRAY, (50, y_ui+5, 30, 30))  # 10 + 5*2 + 30 = 50
    pygame.draw.rect(config.janela.get_screen(), GRAY, (85, y_ui+5, 30, 30))  # 10 + 5*3 + 30*2 = 85
    pygame.draw.rect(config.janela.get_screen(), GRAY, (120, y_ui+5, 30, 30)) # 10 + 5*4 + 30*3 = 120
    pygame.draw.rect(config.janela.get_screen(), GRAY, (155, y_ui+5, 30, 30))  # 10 + 5*5 + 30*4 = 155

    # SEGUNDA LINHA
    pygame.draw.rect(config.janela.get_screen(), GRAY, (15,  y_ui+5*2 + 30, 30, 30))  
    pygame.draw.rect(config.janela.get_screen(), GRAY, (50,  y_ui+5*2 + 30, 30, 30)) # y_ui + 5*2 + 30
    pygame.draw.rect(config.janela.get_screen(), GRAY, (85,  y_ui+5*2 + 30, 30, 30))
    pygame.draw.rect(config.janela.get_screen(), GRAY, (120, y_ui+5*2 + 30, 30, 30))
    pygame.draw.rect(config.janela.get_screen(), GRAY, (155, y_ui+5*2 + 30, 30, 30))

def barra_xp():
    barra_xp_width = config.janela.width
    barra_xp_height = 50

    # DESENHA A BARRA DE XP VAZIA
    pygame.draw.rect(config.janela.get_screen(), BLACK, (0,0, barra_xp_width, barra_xp_height))
    pygame.draw.rect(config.janela.get_screen(), (255,249,89), (0,0, barra_xp_width, barra_xp_height),2)
    
    # MOSTRA O NÍVEL DO JOGADOR
    config.janela.draw_text( "LVL " + str(player.level), barra_xp_width - 70, barra_xp_height/4 , size = 25, color = WHITE, font_name = FONTE, bold = False, italic = False)

    # MOSTRA A QTD DE INIMIGOS MORTOS
    # Código temporário, depois aperfeiçoar
    caveira = Sprite("assets/ui_caveira.png")
    caveira.set_position(config.janela.width - caveira.width -  10, y_ui)
    caveira.draw()
    # Depois ver como colocar a posição dos números corretamente, sem ficar entrando dentro do desenho da caveira quando o número fica grande demais
    config.janela.draw_text(str(player.inimigos_mortos), caveira.x - 20, caveira.y + 2, size = 25, color = WHITE, font_name = FONTE, bold = False, italic = False)

    mostrar_cronometro()
    mostrar_itens()

    # Mostra barra de vida do player
    # Código temporário
    pygame.draw.rect(config.janela.get_screen(), BLACK, (player.player_sprite.x - 100/4, 
                                                         player.player_sprite.y + player.player_sprite.height + 5, 
                                                         100, 20))
    
    pygame.draw.rect(config.janela.get_screen(), RED, (player.player_sprite.x - 100/4 + 2,
                                                       player.player_sprite.y + player.player_sprite.height + 5 + 2,
                                                       96, 16))