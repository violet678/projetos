import pygame
import pgzrun
from pgzero.builtins import Actor
WIDTH =700
HEIGHT = 400
FPS = 30
TITLE = 'Aventuras de Hu Tao'

fundo = Actor('fundo', )  # imagem deve estar em images/fundo.png
player = Actor('player', (300, 50), size=(30,30)) 

def draw():
    fundo.draw()
    player.draw()

def upadate():
   if player.x > 50:
     player.x = player.x - 5
   else:
        player.x = player.x + 5

        
pgzrun.go()