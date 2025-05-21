from PPlay.sprite import *

import config

player_sprite = None
VELOCIDADE = 500

hp = 100
xp = 0
level = 0
inimigos_mortos = 0

def spawn():
    global player_sprite
    player_sprite = Sprite("assets/curupira.png", frames = 2)
    player_sprite.set_loop(0)
    player_sprite.set_total_duration(0)
    player_sprite.set_position(
        (config.janela.width-player_sprite.width)/2, 
        (config.janela.height - player_sprite.height)/2
    )

def draw():
    global player_sprite
    player_sprite.draw()

def change_side(side):
    if side == "LEFT":
        player_sprite.set_curr_frame(1)
    elif side == "RIGHT":
        player_sprite.set_curr_frame(0)