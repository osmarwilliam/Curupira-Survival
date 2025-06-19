import pygame

def game_over(game_sys):
    game_sys["WINDOW"].set_background_color([50,10,10])

    text_surface = pygame.font.SysFont('Tahoma', 50).render("GAME OVER", True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.centerx = game_sys["WINDOW"].width // 2
    text_rect.centery = game_sys["WINDOW"].height // 2
    game_sys["WINDOW"].draw_text("GAME OVER", text_rect.x, text_rect.y, size = 50, color = (255,255,255), font_name = 'Tahoma', bold = True, italic = False) 
    
    game_sys["WINDOW"].update()

    if game_sys["KEYBOARD"].key_pressed("ESC"):
        game_sys["STATE_SWITCHER"] = "MENU"