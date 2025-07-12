from PPlay.sprite import *
from PPlay.collision import Collision
from PPlay.sound import *

from ui import desenhar_ui
import utils
import player
import enemies
import objects
import waves


cam_offset = [0,0]

start_time = None  
delta_t = None

# 0 -> Desativado; 1 -> Ativado
manual_mode = 0

# Efeitos sonoros
hitSound = Sound("assets/audio/hit.wav")
xpSound = Sound("assets/audio/xp.wav")

def update_scenario(): 
    """
    Atualiza as coordenadas reais de cada objeto e inimigo no cenário
    Obs. 1: Coordenada real -> A coordenada de fato do objeto
            Coordenada corrigida com offset -> A coordenada de onde o objeto está na tela corrigido com o offset da câmera

    Obs. 2: Coordenadas reais de objetos estáticos não são atualizadas pois eles não se movimentam
    
    Args: 
        delta_t: delta time da janela
    """
    global delta_t

    for object in objects.objects_list:
        if object["TYPE"] == "ARROW":
            object["X"] += object["DIR_X"] * object["SPEED"] * delta_t
            object["Y"] += object["DIR_Y"] * object["SPEED"] * delta_t

def draw_scenario(): 
    """ 
    Desenha os sprites nas coordenadas corrigidas com o offset
    Obs.: Coordenada corrigida com offset -> A coordenada de onde o objeto está na tela corrigido com o offset da câmera
    """
    for object in objects.objects_list:
        object["SPRITE"].set_position(object["X"] - cam_offset[0], object["Y"] - cam_offset[1])
        object["SPRITE"].draw()

        if object["TYPE"] == "XP":
            object["SPRITE"].update()

    for enemy in enemies.enemies_list: # TODO: Ajeitar inversão do sprite
        enemy["SPRITE"].set_position(enemy["X"] - cam_offset[0], enemy["Y"] - cam_offset[1])
        enemy["SPRITE"].update()
        enemy["SPRITE"].draw()

def collision_detection(window): # Realmente é necessário passar esse window?
    """
    Detecta se houve alguma colisão no jogo
    """
    global hitSound

    # P/a ficar menos verboso
    player_sprite = player.player["SPRITE"]
    # TODO: otimizar a detecção de colisão igual o do space invaders
    # TODO: Colisão entre sprites tá muito bugada, parece até que o collided perfect não tá funcionando
    for object in objects.objects_list:
        if object["TYPE"] == "ARROW":
            X_MIN, X_MAX = player_sprite.x - window.width, player_sprite.x + window.width
            Y_MIN, Y_MAX = player_sprite.y - window.height, player_sprite.y + window.height
            
            # Primeiro verifica se atingiu algum inimigo
            for enemy in enemies.enemies_list:
                if object["SPRITE"].collided_perfect(enemy["SPRITE"]):
                    objects.drop_xp(enemy)
                    objects.objects_list.remove(object)
                    enemies.enemies_list.remove(enemy)
                    player.player["ENEMIES_KILLED"] += 1
                    break

            # Verifica se saiu dos limites da "tela". Não preciso me preocupar com o tamanho exato do sprite, já que essa remoção não será vista pelo jogador
            if not(X_MIN <= object["SPRITE"].x <= X_MAX and Y_MIN <= object["SPRITE"].y <= Y_MAX): 
                objects.objects_list.remove(object)

        elif object["TYPE"] == "XP":
            if object["SPRITE"].collided(player_sprite):
                player.player["XP"] += object["VALUE"]
                xpSound.play()
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
                hitSound.play()
                enemy["LAST-ATK"] = pygame.time.get_ticks()

def run(game_sys):
    global start_time, delta_t
    start_time = pygame.time.get_ticks()
    
    # P/a o código ficar menos verboso e evitar erros de digitação
    WINDOW = game_sys["WINDOW"]
    KEYBOARD = game_sys["KEYBOARD"]
    MOUSE = game_sys["MOUSE"]

    player.spawn(WINDOW)
    
    cam_offset[0] = player.player["SPRITE"].x - WINDOW.width // 2
    cam_offset[1] = player.player["SPRITE"].y - WINDOW.height // 2
    
    backgroundMusic = Sound("assets/audio/bg1_the-gensokyo-the-gods-loved.mp3")
    backgroundMusic.loop = True
    backgroundMusic.play()

    while True:
        delta_t = WINDOW.delta_time()

        # TODO: FAZER A MÚSICA DE FUNDO PAUSAR QUANDO APERTAR O BOTÃO DO MENU
        if KEYBOARD.key_pressed("ESC"):
            game_sys["STATE_SWITCHER"] = "MENU"
            return 0

        player.input(KEYBOARD, MOUSE)

        utils.draw_background(WINDOW, cam_offset)

        waves.auto_wave(WINDOW)
        collision_detection(WINDOW)
        update_scenario()
        draw_scenario()

        if player.player["HP"] <= 0:
            backgroundMusic.stop()
            Sound("assets/audio/game-over.wav").play()
            utils.reset_game()
            game_sys["STATE_SWITCHER"] = "GAME_OVER"
            return 0

        player.update_info()
        player.draw() 

        if enemies.enemies_list != []:
            global manual_mode
            if not manual_mode: player.auto_attack(WINDOW, enemies.enemies_list)
            enemies.think(cam_offset, delta_t)

        desenhar_ui(WINDOW, player.player)
        #utils.draw_version(WINDOW)
        #WINDOW.clear()
        WINDOW.update()
        