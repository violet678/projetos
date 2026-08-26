import pgzrun
from pgzero.builtins import Actor


#configurações do jogo
WIDTH = 1050
HEIGHT = 650
FPS = 60
TITLE = "Meu Jogo com Pygame"

from pgzero.builtins import Actor

#definiçoes de frames 
fundo = Actor('fundo')  
personagem = Actor('player', (180,400), size=(100,100))
lança = Actor('lança.xiao', (1500, 540))
hutao_hurt = Actor('hu_tao_hurt')
def draw():
    screen.clear()
    fundo.draw()
    personagem.draw()
    lança.draw()  

#animação
def update():
    #global personagem
    #personagem.x = personagem.x +5
    
   
    if lança.x > -50:
      lança.x = lança.x - 5
    # Declare uma condição else
    else:
        lança.x = WIDTH + 20

#controles
    if keyboard.LEFT and personagem.x >0:
      personagem.image = "player"
      personagem.x -= 10
    if keyboard.RIGHT and personagem.x < 1500:
      personagem.image = "player"
      personagem.x += 10
    if keyboard.DOWN and personagem.y < 650:
      personagem.y += 10

#colisão
    if personagem.colliderect(lança):
      personagem.image = "hu_tao_hurt"

  

  


#pulo
def on_key_down(key):
    # Pulo com seta para cima, W ou espaço
    if (key == keys.UP or key == keys.W or key == keys.SPACE) and personagem.y == 400:
        personagem.y = 10  # Define a posição inicial do pulo
        animate(
            personagem, 
            tween='linear', 
            duration=2, 
            y=400 )

      
      

pgzrun.go()