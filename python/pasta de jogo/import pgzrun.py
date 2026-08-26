import pgzrun
from pgzero.builtins import Actor


#definiçoes
FPS = 30
WIDTH = 800
HEIGHT = 600

#fundo e inimigo
Fundo = Actor("space")
inimigo = Actor("ship", (400, 300))
bonus_1 = Actor("bonus", (100, 80))
bonus_2 = Actor("bonus", (100, 180))
#variaveis
count = 0
hp = 100
damage = 1
price1 = 20
price2= 50

def draw():
    screen.blit("space", (0, 0))
    inimigo.draw()
    bonus_1.draw()
    bonus_2.draw()
    screen.draw.text(str(hp), center = (400, 130), fontsize = 30, color = "white", background = "#DC143C")
    screen.draw.text(str(count), center = (750, 50), fontsize = 30, color = "white")
    screen.draw.text("bonus 1: 1 de dano a cada 2 segundos(20 pontos)", center=(100, 80), color="#DC143C", fontsize = 20)
    screen.draw.text("bonus 2:5 pontos a cada 2 segundos(50 pontos)", center=(100, 180), color="#DC143C", fontsize = 20)
    

#aparecendo um inimigo novo
def update():
    global hp
    if hp <=0:
        hp = 100


#processando os cliques
def on_mouse_down(button, pos):
    global count, damage, hp
    if button == mouse.LEFT:
        if inimigo.collidepoint(pos):
            count += 1
            hp -= damage
    #clicando no bonus 1
    elif bonus_1.collidepoint(pos):
        if count >= price1:
            schedule_interval(price1, 2)
            count -=price1
    #clicando no bonus 2
    elif bonus_2.collidepoint(pos): 
        if count >= price2:
            schedule_interval(price2, 2)
            count -=price2

pgzrun.go()