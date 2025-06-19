import pygame
from PPlay.gameimage import *
from PPlay.sprite import *

import states.game as game
from player import player

WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (88,97,98)
RED = (173, 24, 24)

FONTE = 'Tahoma'

# "segunda camda" da UI, logo embaixo da barra de XP
y_ui = 60  # 60 = barra_xp_height + 10 de padding
 
def mostrar_cronometro(janela): # Mostra na tela há quanto tempo o jogador iniciou a partida
    tempo_atual = pygame.time.get_ticks() - game.start_time
    segundos_decorridos = tempo_atual // 1000 # Converte em segundos

    # Formata o tempo (MM:SS)
    minutos = segundos_decorridos // 60
    segundos = segundos_decorridos % 60
    cronometro = f"{minutos:02d}:{segundos:02d}"

    # Renderiza o texto
    text_surface = pygame.font.SysFont(FONTE, 40).render(cronometro, True, WHITE)
    text_rect = text_surface.get_rect() # Vê o tamanho do texto renderizado
    text_rect.centerx = janela.width //2 # Posição X

    # Desenha na tela o texto
    janela.draw_text(cronometro, text_rect.x, y_ui, size = 40, color = WHITE, font_name = FONTE, bold = True, italic = False)

def mostrar_itens(janela): # Desenha os "contâiners" dos itens
    # Código temporário
    pygame.draw.rect(janela.get_screen(), BLACK, (10, y_ui, 30*5 + 5*6, 30*2 + 5*3))
    
    pygame.draw.rect(janela.get_screen(), GRAY, (15, y_ui+5, 30, 30))
    pygame.draw.rect(janela.get_screen(), GRAY, (50, y_ui+5, 30, 30))  # 10 + 5*2 + 30 = 50
    pygame.draw.rect(janela.get_screen(), GRAY, (85, y_ui+5, 30, 30))  # 10 + 5*3 + 30*2 = 85
    pygame.draw.rect(janela.get_screen(), GRAY, (120, y_ui+5, 30, 30)) # 10 + 5*4 + 30*3 = 120
    pygame.draw.rect(janela.get_screen(), GRAY, (155, y_ui+5, 30, 30))  # 10 + 5*5 + 30*4 = 155

    # SEGUNDA LINHA
    pygame.draw.rect(janela.get_screen(), GRAY, (15,  y_ui+5*2 + 30, 30, 30))  
    pygame.draw.rect(janela.get_screen(), GRAY, (50,  y_ui+5*2 + 30, 30, 30)) # y_ui + 5*2 + 30
    pygame.draw.rect(janela.get_screen(), GRAY, (85,  y_ui+5*2 + 30, 30, 30))
    pygame.draw.rect(janela.get_screen(), GRAY, (120, y_ui+5*2 + 30, 30, 30))
    pygame.draw.rect(janela.get_screen(), GRAY, (155, y_ui+5*2 + 30, 30, 30))

def desenhar_barra_xp(janela):
    barra_xp_width = janela.width
    barra_xp_height = 50

    #print("PLAYER XP: " + str(player["XP"]))
    xp_ratio = min(player["XP"] / player["XP_MAX"], 1)
    xp_fill_width = int(barra_xp_width * xp_ratio)

    # DESENHA A BARRA DE XP VAZIA
    pygame.draw.rect(janela.get_screen(), BLACK, (0,0, barra_xp_width, barra_xp_height))
    pygame.draw.rect(janela.get_screen(), (255,249,89), (0,0, barra_xp_width, barra_xp_height),2)

    # PREENCHE A BARRA
    pygame.draw.rect(janela.get_screen(), (143,250,55), (0,0, xp_fill_width, barra_xp_height))

def desenhar_barra_vida(janela):
    largura_barra_hp = 100
    hp_max = 100
    
    # DESENHA A BARRA DE HP VAZIA
    pygame.draw.rect(janela.get_screen(), BLACK, (player["SPRITE"].x - 100/4, 
                                                  player["SPRITE"].y + player["SPRITE"].height + 5, 
                                                  largura_barra_hp, 20))
    
    barra_preenchida = (player["HP"] / hp_max) * largura_barra_hp

    # DESENHA A BARRA COM A VIDA ATUAL DO JOGADOR
    pygame.draw.rect(janela.get_screen(), RED, (player["SPRITE"].x - 100/4, 
                                                player["SPRITE"].y + player["SPRITE"].height + 5,
                                                barra_preenchida, 20))

def mostrar_inimigos_mortos(janela):
    caveira = GameImage("assets/ui_caveira.png")
    caveira.set_position(janela.width - caveira.width -  10, y_ui)
    caveira.draw()

    text = pygame.font.SysFont('Tahoma', 25).render(str(player["ENEMIES_KILLED"]), True, (255,255,255))
    text_rect = text.get_rect()
    
    janela.draw_text(str(player["ENEMIES_KILLED"]), 
                     caveira.x - text_rect.width - 10, 
                     caveira.y + 2, 
                     size = 25, 
                     color = WHITE, 
                     font_name = FONTE, 
                     bold = False, 
                     italic = False)

def desenhar_ui(janela, player):
    barra_xp_height = 50
    
    desenhar_barra_xp(janela)

    # MOSTRA O NÍVEL DO JOGADOR
    janela.draw_text( "LVL " + str(player["LEVEL"]), janela.width - 70, barra_xp_height/4 , size = 25, color = WHITE, font_name = FONTE, bold = False, italic = False)

    # MOSTRA A QTD DE INIMIGOS MORTOS
    mostrar_inimigos_mortos(janela)

    mostrar_cronometro(janela)
    mostrar_itens(janela)

    # Mostra barra de vida do player
    desenhar_barra_vida(janela)
