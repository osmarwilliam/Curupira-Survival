import pygame
import globals,objects,player,enemies,waves
from PPlay.gameimage import *

DELAY_ENTRE_CLIQUES = 300
ultimo_clique = 0

def draw_version(window):
    game_version = "ALPHA VERSION"

    window.draw_text(game_version, 
                     5, 
                     window.height - 30, 
                     size = 25, 
                     color = (255,255,255), 
                     font_name = 'Tahoma', 
                     bold = False, 
                     italic = False)

def clicked(mouse, button):
    global ultimo_clique, DELAY_ENTRE_CLIQUES

    tempo_atual = pygame.time.get_ticks()
    clicou = mouse.is_button_pressed(1) and mouse.is_over_object(button) and tempo_atual - ultimo_clique > DELAY_ENTRE_CLIQUES

    if clicou: ultimo_clique = tempo_atual
    return clicou

def draw_sprite(object):
    if (object["FACING_RIGHT"]):
        object["SPRITE"].draw()
    else:
        sprite_width = object["SPRITE"].width
        sprite_height = object["SPRITE"].height
        image = object["SPRITE"].image

        # Obs.: Fiz uma mistureba aqui com o código do pplay com o pygame.transform pra conseguir virar o sprite
        # Clips the frame (rect on the image)
        clip_rect = pygame.Rect(object["SPRITE"].get_curr_frame()*sprite_width,
                                0,
                                sprite_width,
                                sprite_height
                                )

        # Updates the pygame rect based on new positions values
        object["SPRITE"].rect = pygame.Rect(object["SPRITE"].x, object["SPRITE"].y, sprite_width, sprite_height)

        flipped_surface = pygame.transform.flip(image, True, False)
        globals.WINDOW.get_screen().blit(flipped_surface, object["SPRITE"].rect, area=clip_rect)

def draw_background(window, cam_offset):
    """
    window_width = window.width
    window_height = window.height
    
    bac = GameImage("assets/grass.png")
    x = 0
    y = 0

    while(y < window_height):
        while(x < window_width):
            bac.set_position(x - cam_offset[0],y - cam_offset[1])
            bac.draw()

            x += bac.width
        y += bac.height
        x = 0
    """
    # TODO: ENTENDER PQ ISSO AQ FUNCIONA
    tile = GameImage("assets/grass.png")
    tile_w, tile_h = tile.width, tile.height

    # Calcula o início do grid para cobrir toda a tela
    start_x = -((cam_offset[0]) % tile_w)
    start_y = -((cam_offset[1]) % tile_h)

    # Quantos tiles cabem na tela (+2 para garantir cobertura)
    tiles_x = window.width // tile_w + 2
    tiles_y = window.height // tile_h + 2

    for i in range(tiles_x):
        for j in range(tiles_y):
            x = start_x + i * tile_w
            y = start_y + j * tile_h
            tile.set_position(x, y)
            tile.draw()

def reset_game():
    global start_time, delta_t
    start_time = None
    delta_t = None

    # Volta os dados do jogo p/a o estado inicial  
    player.reset()
    objects.reset()
    enemies.reset()
    waves.reset()