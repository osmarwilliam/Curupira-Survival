from utils import clicou

def mostrar_menu(sys_state):
    WINDOW = sys_state["WINDOW"]

    WINDOW.set_background_color([22,158,38])
        
    botao_jogar = sys_state["SPRITES"]["botao_jogar"]

    botao_lar = botao_jogar.width
    botao_alt = botao_jogar.height
        
    botao_jogar.set_position((WINDOW.width - botao_lar)/2, WINDOW.height/2 - botao_alt - 20/2)
    
    botao_sair = sys_state["SPRITES"]["botao_sair"]
    botao_sair.set_position( (WINDOW.width - botao_lar)/2, WINDOW.height/2 + 20/2)

    botao_jogar.draw()
    botao_sair.draw()
        
    WINDOW.update()

    #LÓGICO
    if clicou(sys_state["MOUSE"], botao_jogar):
        sys_state["controlador"] = "JOGO"
    elif clicou(sys_state["MOUSE"], botao_sair):
        WINDOW.close()
