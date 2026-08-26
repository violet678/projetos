import pgzrun
from pgzero.builtins import Actor

#definiçoes
FPS = 30
WIDTH = 800
HEIGHT = 600


#variaveis
reputação = 500
vida = 100
sanidade = 50
ataque = 3
defesa = 3
dinheiro = 1000


#fundo
Fundo = Actor ('chão')

Fundo2 = Actor ('origbig')
fundo3 = Actor('chão de grama')
detalhes = Actor('walls_floor')
parede = Actor('parede', (1000, 300))
parede2 = Actor('parede', (1700, 300))


player = Actor ('hero', (400, 300))
fundo_atual = 1

#parte grafica do jogo
def draw():
    global fundo_atual
    screen.draw.text(str(reputação), center=(200, 200), color="white", fontsize=20)
    if fundo_atual == 1:
        screen.blit("chão", (WIDTH, HEIGHT))
        Fundo.draw()
        parede.draw()
        parede2.draw()

    elif fundo_atual == 2:
        screen.blit("origbig2", (WIDTH, HEIGHT))
        Fundo2.draw()
    
    elif fundo_atual == 3:
        screen.blit("chão de grama", (WIDTH, HEIGHT))
        fundo3.draw()
    # Draw the correct background based on movement
    
    player.draw()
    


def update():
    global fundo_atual
    # Movimentação do personagem
    if keyboard.left or keyboard.A and player.x > 50:  # Impede que o player saia pela esquerda
        player.x -= 5
        player.image = 'hero left'  
    if keyboard.right or keyboard.D and player.x < WIDTH - 50:  # Impede que o player saia pela direita
        player.x += 5
        player.image = 'hero right'
    if keyboard.down  or keyboard.S and player.y < HEIGHT - 50:  # Impede que o player saia pela parte inferior
        player.y += 5
        player.image = 'hero'
    if keyboard.up  or keyboard.W  and player.y > 50:  # Impede que o player saia pela parte superior
        player.y -= 5
        player.image = 'hero'

    # Transição entre os fundos
    if fundo_atual == 1 and player.x <= 50:
        fundo_atual = 2
        player.x = WIDTH - 50
    elif fundo_atual == 2 and player.x >= WIDTH - 50:
        fundo_atual = 1
        player.x = 50
    elif fundo_atual == 1 and player.y >= HEIGHT - 50:
        fundo_atual = 3
        player.y = 50 
    elif fundo_atual == 3 and player.y <= 50:
        fundo_atual = 1
        player.y = HEIGHT - 50
    

          # Reposiciona o player no lado esquerdo da cena anterior

pgzrun.go()