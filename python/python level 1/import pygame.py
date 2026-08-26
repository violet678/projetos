import pygame
import math
# Inicializando módulos de Pygame
pygame.init()
# Criando uma janela com o título “Olá, mundo!”
janela = pygame.display.set_mode((400, 300))
pygame.display.set_caption("olá mundo")
lista_var = [1,2,3,]
#o valor sum() de Python:recebe uma lista (neste caso) e devolve seus elementos somados
sum(lista_var) #retornará 6
#função sqrt() de Python: recebe um número e devolve sua raiz quadrada
math.sqirt(16) #retornará4.0
#metodo append() de Python: adiciona um elemento ao final de uma lista
lista_var.append(4) #lista_var agora será [1, 2, 3, 4]

print(lista_var)

# Variável de controle do loop
deve_continuar = True
# Loop do jogo
while deve_continuar:
# Checando eventos
    for event in pygame.event.get():
# Se for um evento QUIT
        if event.type == pygame.QUIT:
            deve_continuar = False
# Encerrando módulos
pygame.quit()