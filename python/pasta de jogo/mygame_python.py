#bibliotecas
import pgzrun
from pgzero.builtins import Actor
from pgzero.keyboard import keys

import json
#----------------------------------------------------1
# definições 
FPS = 30
WIDTH = 800
HEIGHT = 600

#----------------------------------------------------2
# variáveis
reputacao = 500
vida = 100
sanidade = 50
intelecto = 10
dinheiro = 1000
# texto / estado para interações
texto_atual = [
    "voce ve uma mesa feita de madeira com formato circular",
    "com alguns livros encima dela"
]
study_state = None  # None | 'prompt' | 'done'
save_state = None  # None | 'prompt' | 'done'
#----------------------------------------------------3
# cenário e sprites
Fundo = Actor('chao')
Fundo2 = Actor('origbig')
fundo3 = Actor('chao_de_grama')
detalhes = Actor('walls_floor')
parede = Actor('parede', (1000, 300))
parede2 = Actor('parede', (1700, 300))
fundo_atual = 1
#----------------------------------------------------4
player = Actor('hero', (400, 300))
table = Actor('table_remove_bg', (205, 400))
book = Actor('book_remove_bg', (205, 310))
caixa_de_texto = Actor('caixa_de_texto', (400, 550))
seta = Actor('seta', (750, 550))
save_star = Actor('save_star', (450, 50))

#--------------------------------------------------5
# parte gráfica do jogo
def draw():
    global fundo_atual

    if fundo_atual == 1:
        screen.blit("chao", (0, 0))
        Fundo.draw()
        parede.draw()
        parede2.draw()
        save_star.draw()
    elif fundo_atual == 2:
        screen.blit("chao", (0, 0))
        Fundo.draw()
        table.draw()
        book.draw()
    elif fundo_atual == 3:
        screen.blit("chao_de_grama", (0, 0))
        fundo3.draw()

    player.draw()
 #status
#----------------------------------------------------6
    screen.draw.text(str(reputacao), center=(200, 200), color="white", fontsize=20)
    screen.draw.text("vida:" + str(vida), (710, 10), color="Black", fontsize=30)
    screen.draw.text("sanidade:" + str(sanidade), (680, 40), color="Black", fontsize=30)
    screen.draw.text("intelecto:" + str(intelecto), (680, 70), color="Black", fontsize=30)
    screen.draw.text("dinheiro:" + str(dinheiro), (665, 100), color="Black", fontsize=30)
#----------------------------------------------------7
    if fundo_atual == 1  and player.colliderect(save_star):
        caixa_de_texto.draw()
        seta.draw()
        if save_state in ('prompt', 'done'):
            if isinstance(texto_atual, (list, tuple)):
                lines = texto_atual
            elif texto_atual is None:
                lines = []
            else:
                lines = [str(texto_atual)]
            for i, linha in enumerate(lines):
                screen.draw.text(str(linha), (200, 525 + i * 40), color="Black", fontsize=20)
        
        else:
            screen.draw.text("deseja salvar o jogo?", (200, 525), color="Black", fontsize=20)

    if fundo_atual == 2 and player.colliderect(table):
        caixa_de_texto.draw()
        seta.draw()
        # Se estivermos no prompt (ou já concluído), mostra texto_atual;
        # caso contrário mostra a descrição fixa do objeto.
        if study_state in ('prompt', 'done'):
            if isinstance(texto_atual, (list, tuple)):
                lines = texto_atual
            elif texto_atual is None:
                lines = []
            else:
                lines = [str(texto_atual)]
            for i, linha in enumerate(lines):
                screen.draw.text(str(linha), (200, 525 + i * 40), color="Black", fontsize=20)
        else:
            screen.draw.text("você vê uma mesa feita de madeira com formato circular", (200,525), color="Black", fontsize=20)
            screen.draw.text("com alguns livros em cima dela", (200,565), color="Black", fontsize=20)



#----------------------------------------------------8
def on_mouse_down(pos, button):
    global texto_atual, study_state, save_state
    # assinatura correta: (pos, button)
    # só altera quando estiver no fundo 2 e próximo da mesa
    if button == mouse.LEFT and fundo_atual == 2 and player.colliderect(table):
        # aceita clique na seta ou na própria caixa de texto (área maior)
        if seta.collidepoint(pos) or caixa_de_texto.collidepoint(pos):
            texto_atual = ["Deseja estudar?", "aperte Z para sim ou X para nao"]
            study_state = 'prompt'
    
    if button == mouse.LEFT and fundo_atual == 1 and player.colliderect(save_star):
        if seta.collidepoint(pos) or caixa_de_texto.collidepoint(pos):
            texto_atual = ["Z para sim e X para não"]
            save_state = 'prompt'

#----------------------------------------------------9
def update():
    global fundo_atual
    # Movimentação do personagem
    if (keyboard.left or keyboard.A) and player.x > 50:
        player.x -= 5
        player.image = 'hero_left'
    if (keyboard.right or keyboard.D) and player.x < WIDTH - 50:
        player.x += 5
        player.image = 'hero_right'
    if (keyboard.down or keyboard.S) and player.y < HEIGHT - 50:
        player.y += 5
        player.image = 'hero'
    if (keyboard.up or keyboard.W) and player.y > 50:
        player.y -= 5
        player.image = 'hero'

#----------------------------------------------------10

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
#----------------------------------------------------11
    

def on_key_down(key):
    global texto_atual, study_state
    # responde a teclas apenas quando estamos no prompt (não depende de colisão)
    if study_state == 'prompt':
        if key == keys.Z:
            texto_atual = ["Você estuda os livros e aumenta seu intelecto.", "+3 intelecto"]
            intelecto += 3
            study_state = 'done'
        elif key == keys.X:
            texto_atual = ["Você decide não estudar."]
            study_state = 'done'

    






pgzrun.go()