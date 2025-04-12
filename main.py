from PPlay.window import *

def init():
    global janela;
    
    janela = Window(1000,800)
    janela.set_title("Curupira Survival")

init()

while True:
    janela.set_background_color([100,100,100])

    janela.update()
