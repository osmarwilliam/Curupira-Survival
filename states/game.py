from PPlay.sprite import *
from PPlay.collision import Collision
from PPlay.sound import *

from ui import desenhar_ui
import globals
import utils
import player
import enemies
import objects
import waves
from states.bestiario import atualizar_abates

cam_offset = [0,0]

start_time = None  
delta_t = None

death_count = {
    "JAVALI" : 0,
    "LENHADOR" : 0,
    "CACADOR" :0
} 

def update_scenario(): 
    """
    Atualiza as coordenadas reais de cada objeto e inimigo no cenário
    Obs. 1: Coordenada real -> A coordenada de fato do objeto
            Coordenada corrigida com offset -> A coordenada de onde o objeto está na tela corrigido com o offset da câmera

    Obs. 2: Coordenadas reais de objetos estáticos não são atualizadas pois eles não se movimentam
    """
    global delta_t

    for object in objects.objects_list:
        if object["TYPE"] == "FIREBALL":
            object["X"] += object["DIR_X"] * object["SPEED"] * delta_t
            object["Y"] += object["DIR_Y"] * object["SPEED"] * delta_t

def draw_scenario(): 
    """ 
    Desenha os sprites nas coordenadas corrigidas com o offset
    Obs.: Coordenada corrigida com offset -> A coordenada de onde o objeto está na tela corrigido com o offset da câmera
    """
    for object in objects.objects_list:
        object["SPRITE"].set_position(object["X"] - cam_offset[0], object["Y"] - cam_offset[1])

        if object["TYPE"] == "ARROW":
            sprite = object["SPRITE"]

            rotated_surface = object["ROTATED_SURFACE"]
            rect = rotated_surface.get_rect(center=(sprite.x, sprite.y))

            globals.WINDOW.get_screen().blit(rotated_surface, rect)
        elif object["TYPE"] == "FIREBALL":
            object["SPRITE"].update()
            object["SPRITE"].draw()
        elif object["TYPE"] == "XP":
            object["SPRITE"].update()
            object["SPRITE"].draw()

    for enemy in enemies.enemies_list: # TODO: Ajeitar inversão do sprite
        enemy["SPRITE"].set_position(enemy["X"] - cam_offset[0], enemy["Y"] - cam_offset[1])
        enemy["SPRITE"].update()

        # Depois ajeitar esse cálculo aqui
        if enemy["SPRITE"].x > player.player["SPRITE"].x:
            enemy["FACING_RIGHT"] = 0
        else:
            enemy["FACING_RIGHT"] = 1

        utils.draw_sprite(enemy)

def collision_detection():
    WINDOW = globals.WINDOW

    # P/a ficar menos verboso
    player_sprite = player.player["SPRITE"]
    # TODO: otimizar a detecção de colisão igual o do space invaders
    # TODO: Colisão entre sprites tá muito bugada, parece até que o collided perfect não tá funcionando
    for object in objects.objects_list:
        if object["TYPE"] == "FIREBALL":
            X_MIN, X_MAX = player_sprite.x - WINDOW.width, player_sprite.x + WINDOW.width
            Y_MIN, Y_MAX = player_sprite.y - WINDOW.height, player_sprite.y + WINDOW.height
            
            # VERIFICAÇÃO DE COLISÃO COM INIMIGO
            for enemy in enemies.enemies_list:
                enemy_sprite = enemy["SPRITE"]
                fireball_sprite = object["SPRITE"]

                # BUGADO
                verificavel = not(enemy_sprite.x > fireball_sprite.x + fireball_sprite.width or
                                  enemy_sprite.x + enemy_sprite.width < fireball_sprite.x or
                                  enemy_sprite.y > fireball_sprite.y + fireball_sprite.height or
                                  enemy_sprite.y + enemy_sprite.height < fireball_sprite.y
                                  )

                if verificavel and object["SPRITE"].collided_perfect(enemy["SPRITE"]):
                    print("VERIFICAVEL")
                    objects.drop_xp(enemy)
                    objects.objects_list.remove(object)
                    enemies.enemies_list.remove(enemy)
                    player.player["ENEMIES_KILLED"] += 1
                    death_count[enemy["TYPE"]] += 1
                    break
            # Verifica se saiu dos limites da "tela". Não preciso me preocupar com o tamanho exato do sprite, já que essa remoção não será vista pelo jogador
            if not(X_MIN <= object["SPRITE"].x <= X_MAX and Y_MIN <= object["SPRITE"].y <= Y_MAX): 
                objects.objects_list.remove(object)
        elif object["TYPE"] == "XP" and object["SPRITE"].collided(player_sprite):
                player.player["XP"] += object["VALUE"]
                globals.XP_SOUND.play()
                objects.objects_list.remove(object)
    
    for enemy in enemies.enemies_list:
        verificavel = True
        if enemy["SPRITE"].x > player_sprite.x + player_sprite.width:
            verificavel = False
        elif enemy["SPRITE"].x + enemy["SPRITE"].width < player_sprite.x:
            verificavel = False
        elif enemy["SPRITE"].y + enemy["SPRITE"].height < player_sprite.y:
            verificavel = False
        elif enemy["SPRITE"].y > player_sprite.y + player_sprite.height:
            verificavel = False

        if verificavel and pygame.time.get_ticks() - enemy["LAST-ATK"] > enemy["ATK-COOLDOWN"]:
            if enemy["SPRITE"].collided_perfect(player_sprite):
                player.player["HP"] -= enemy["ATK"]
                globals.HIT_SOUND.play()
                enemy["LAST-ATK"] = pygame.time.get_ticks()

def run():
    global start_time, delta_t
    start_time = pygame.time.get_ticks()
    
    # P/a o código ficar menos verboso e evitar erros de digitação
    WINDOW = globals.WINDOW
    KEYBOARD = globals.KEYBOARD
    MOUSE = globals.MOUSE

    player.spawn()
    
    cam_offset[0] = player.player["SPRITE"].x - WINDOW.width // 2
    cam_offset[1] = player.player["SPRITE"].y - WINDOW.height // 2
    
    globals.BG1 = Sound("assets/audio/bg1_the-gensokyo-the-gods-loved.mp3")
    globals.BG1.loop = True
    globals.BG1.play()
    globals.HIT_SOUND = Sound("assets/audio/hit.wav")
    globals.XP_SOUND = Sound("assets/audio/xp.wav")

    while True:
        delta_t = WINDOW.delta_time()

        # TODO: FAZER A MÚSICA DE FUNDO PAUSAR QUANDO APERTAR O BOTÃO DO MENU
        if KEYBOARD.key_pressed("ESC"):
            globals.current_state = "MENU"
            atualizar_abates(death_count.copy())
            return 0

        player.input(KEYBOARD, MOUSE)
        utils.draw_background(WINDOW, cam_offset)

        waves.auto_wave()
        collision_detection()
        update_scenario()
        draw_scenario()

        if player.player["HP"] <= 0:
            globals.BG1.stop()
            Sound("assets/audio/game-over.wav").play()
            atualizar_abates(death_count.copy())  # Salva os abates
            utils.reset_game()
            globals.current_state = "GAME_OVER"
            return 0

        player.update_info()
        utils.draw_sprite(player.player) 

        if enemies.enemies_list != []:
            if not globals.manual_mode: player.auto_attack(enemies.enemies_list)
            enemies.think(cam_offset, delta_t)

        desenhar_ui(player.player)

        WINDOW.update()
        