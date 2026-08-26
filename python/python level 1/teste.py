#bibliotecas
import time
import random
#apresentação
print("bem vindo ao rpg do jogo das portas (≧∇≦)ﾉ")
input()
input("o jogo das portas é um ""rpg"" de multipla escolha, nessa historia voce poderá ter 3 opçoes de escolha, quer começar?")
input() 
time.sleep(2)
# Inimigos
inimigos = {
    'slime': {'vida': 20, 'ataque': 4},
    'esqueleto': {'vida': 10, 'ataque': 3},
    'zumbi': {'vida': 10, 'ataque': 1},
    'necromante': {'vida': 70, 'ataque': 12},
    'dragao': {'vida': 100, 'ataque': 15}
}

#status iniciais
magia = 5
combate = 5
vida = 35
xp = 0
pontos_de_distribuição = 0
moedas_de_ouro = 0
inimigo_derrotado = ''




#definiçoes de buffs/aumentos
def aumento_de_xp(valor):
    global xp
    xp += valor
    print("Seu XP:", xp)
    

def aumento_de_combate(valor):
    global combate
    combate += valor
    print("Seu combate:", combate)


def aumento_de_magia(valor):
    global magia
    magia += valor
    print("Sua magia:", magia)


def aumento_das_moedas_de_ouro_1(valor):
    global moedas_de_ouro
    moedas_de_ouro +=valor


#status dos inimigos
 
#esqueleto:
vida_esqueleto = 10
ataque_esqueleto = 3

#zumbi:
vida_zumbi = 10
ataque_zumbi = 1

#slime:
vida_slime = 20
ataque_slime = 4

#necromante:
vida_necromante = 70
ataque_necromante = 12

#dragão:
vida_dragão = 100
ataque_dragão = 15

#definiçoes de inimigos/ataques dos inimigos
def inimigo_ataca(nome):
    global vida
    dano = inimigos[nome]['ataque']
    vida -= dano
    print(f"O {nome} atacou você! Sua vida atual: {vida}")
#definiçoes atacando inimigos
def atacar_inimigo(nome):
    global combate
    dano = combate
    inimigo = inimigos[nome]
    inimigo['vida'] -= combate 
    if inimigo['vida'] < 0:  # Evita vida negativa
        inimigo['vida'] = 0
    print(f"Você atacou o {nome}! Vida restante do inimigo: {inimigo['vida']}")
def atacar_magia(nome):
    global magia
    inimigo = inimigos[nome]
    dano = magia
    inimigo['vida'] -= dano
    if inimigo['vida'] < 0:  # Evita vida negativa
        inimigo['vida'] = 0
    print(f"Você atacou o {nome}! Vida restante do inimigo: {inimigo['vida']}")



def atacar_inimigo_escolha():
    escolha_ataque = input('como voce quer atacar seu inimigo? combate ou magia')
    if escolha_ataque == 'combate':
        atacar_inimigo()
    elif escolha_ataque == 'magia':
        atacar_magia()


#subiu de level
def level_1():
    if xp == 10: #type: ignore
        print("parabens, voce subiu de level, voce está no level 1")
        combate = 5
        vida = 35
        vida -=35
        vida += 40
        combate +=3
        magia = 5
        magia +=3

        print("seus status abaixo:")
        print("vida: ", vida)
        print("magia: ", magia)
        print("combate: ", combate)
def level_2():
    if xp == 35: #type: ignore
        print("parabens, voce subiu de nivel, agora voce está no nivel 2") 
        combate = 45
        vida = 20
        vida -=20
        vida += 60
        combate +=7
        magia +=7

        print('seus status abaixo:')
        print('vida:', vida)
        print('combate: ', combate)
        print('magia: ', magia)
def level_3():
    if xp == 50:
        print('parabens, voce está no level 3')
        vida = 40
        vida -=40
        vida +=80
        combate = 52
        combate +=10
        magia = 9
        magia +=10
        
        print('seus status abaixo:')
        print('vida: ', vida)
        print('combate: ', combate)
        print('combate: ', combate)

def level_4():
    if xp == 100:
        print('parabens, voce está no level 4 ')
        vida = 60
        vida -=60
        vida +=100
        combate = 52
        combate +=50
        magia = 19
        magia +=50

        print('sua vida: ', vida)
        print('seu combate: ', combate)
        print('sua magia: ', magia)

def level_5():
    if xp == 120:
        print('parabens, voce está no level 5')
        vida = 90
        vida -=90
        vida -=120
        combate = 102
        combate +=70
        magia = 69
        magia +=70


        print('sua vida atual: ', vida)
        print('seu combate atual: ', combate)
        print('sua magia atual: ', magia)




def portas():
    print("bem vindo ao choice, voce acorda em um lugar com 3 portas, qual porta voce escolhe?🚪🚪🚪, 1, 2 ou 3?")
    escolha = int(input("faça sua escolha"))
    if escolha == 1:
        print('achou uma parede de tijolos,')
        input()
    if escolha == 2:
        print('achou um dragão, morreu')
        input()
    if escolha == 3:
        print('achou a saida')
        input()

#inicio da historia-capitulo 1 😎
print("bem vindo ao choice, voce acorda em um lugar com 3 portas, qual porta voce escolhe?🚪🚪🚪, 1, 2 ou 3?")
escolha = int(input("faça sua escolha"))
if escolha == 1:
    print('achou uma parede de tijolos,')
    time.sleep(2)
    portas()
    
if escolha == 2:
    print('achou um dragão, morreu')
    time.sleep(2)
    portas()

    
if escolha == 3:
    print('achou a saida') 
    

#cidade-capitulo 1 🛣️
print("ao sair de onde voce estava, voce vai até um reino, e chegando lá, um guarda te aborda e te apresenta a cidade, e te pede para escolher entre algumas opçoes")
print("🤺Guarda: agora que voce ja conheçe a cidade, que tal obter um pouco de conhecimento sobre magia, indo até a biblioteca antiga da cidade ou combate?, treinando com o ferreiro?")
print("qual voce escolhe? 1 ou 2")
treino = int(input())
if treino == 1:
    print("parabens, agora voce sabe magia após ir para a biblioteca antiga da cidade")
    magia+=1
    xp+=1
    print('sua magia: ', magia)
    print('seu xp: ', xp)
    input()
if treino == 2:
    print("parabens, agora suas habilidades em combate aumentaram")
    combate+=1
    xp+=1
    print('seu combate: ', combate)
    print('seu xp: ', xp)
    input()

#combate / missão - capitulo 1 ⚔️
# Início da missão
print("Após treinar na vila, você recebe uma missão.")
print("Ela diz para eliminar monstros que atormentam a vila.")
print("Você se depara com: esqueletos, zumbis e slimes.")
print("Quem você quer atacar primeiro? 1 - Zumbis | 2 - Esqueletos | 3 - Slimes")
ataque = int(input("Faça seu ataque: "))

def combate_inimigo(nome):
    global inimigo_derrotado
    escolha_ataque = input("Atacar com (1) Combate ou (2) Magia? ").strip().lower()
    if escolha_ataque == '1' or escolha_ataque == 'combate':
        atacar_inimigo(nome)
        while inimigos[nome]['vida'] > 0 and vida > 0:
            atacar_inimigo(nome)
            if inimigos[nome]['vida'] <= 0:
                print(f"Você derrotou o {nome}!")
                inimigo_derrotado = nome
                aumento_de_xp(3)
                break
            inimigo_ataca(random.choice([i for i in inimigos if i != nome and inimigos[i]['vida'] > 0]))
            aumento_de_xp(3)
    elif escolha_ataque == '2' or escolha_ataque == 'magia':
        atacar_magia(nome)
        while inimigos[nome]['vida'] > 0 and vida > 0:
            atacar_inimigo(nome)
            if inimigos[nome]['vida'] <= 0:
                print(f"Você derrotou o {nome}!")
                inimigo_derrotado = nome
                aumento_de_xp(3)
                break
            inimigo_ataca(random.choice([i for i in inimigos if i != nome and inimigos[i]['vida'] > 0]))
            aumento_de_xp(3)
    else:
        print("Opção inválida! Atacando com combate padrão.")
        atacar_inimigo(nome)
        inimigo_derrotado = nome
        aumento_de_xp(3)

# Primeiro turno
if ataque == 1:
    combate_inimigo('zumbi')
elif ataque == 2:
    combate_inimigo('esqueleto')
elif ataque == 3:
    combate_inimigo('slime')
else:
    print("Opção inválida! Começando pelo zumbi.")
    combate_inimigo('zumbi')

# Segundo turno
if inimigo_derrotado == 'zumbi':
    print("\nEscolha seu próximo alvo:")
    print("1 - Esqueletos | 2 - Slimes")
    ataque2 = int(input(">>> "))
    if ataque2 == 1:
        combate_inimigo('esqueleto')
    elif ataque2 == 2:
        combate_inimigo('slime')
    else:
        print("Opção inválida! Atacando esqueleto.")
        combate_inimigo('esqueleto')
elif inimigo_derrotado == 'esqueleto':
    print("\nRestam zumbis e slimes. Qual você quer atacar?")
    print("1 - Zumbis | 2 - Slimes")
    ataque2 = int(input("Escolha: "))
    if ataque2 == 1:
        combate_inimigo('zumbi')
    elif ataque2 == 2:
        combate_inimigo('slime')
    else:
        print("Opção inválida! Atacando zumbi.")
        combate_inimigo('zumbi')
elif inimigo_derrotado == 'slime':
    print("\nRestam zumbis e esqueletos. Qual você quer atacar?")
    print("1 - Zumbis | 2 - Esqueletos")
    ataque2 = int(input("Escolha: "))
    if ataque2 == 1:
        combate_inimigo('zumbi')
    elif ataque2 == 2:
        combate_inimigo('esqueleto')
    else:
        print("Opção inválida! Atacando zumbi.")
        combate_inimigo('zumbi')


#fim do combate / missão - capitulo 1 ☮️
print("após derrotar o monstro que restava e acabar com todos os monstros, voce recebe a recompensa em 500 moedas de ouro")
aumento_de_xp(3)
print('seu xp atual: ', xp)
print('seu xp: ', xp)
moedas_de_ouro +=500
pontos_de_distribuição +=1
#explicando mecanicas - capitulo 1 💡
time.sleep(3)
print("agora voce desbloqueou novas mecanicas, compras na loja, moedas de ouro, banco e pontos de distribuição")
time.sleep(3)
print("voce ganhará essas recompensas depois de toda missão, dependendo do nivel da missão")
print("voce ganhará uma recompensa maior em moeda de ouro")
input()
print("pontos de distribuição:")
print("são pontos que voce usa para aumentar suas habilidades de magia e combate")
print("depois de toda missão, voce ganha 1 ponto de distribuição, independente do nivel da missão")
print(' ')
level_1()
print('')
input('aperte enter para voltar a historia')

input()
print("voltando para a historia...")
time.sleep(2)
print("voltando para a historia..")
time.sleep(2)
print("voltando para a historia.")
time.sleep(2)
print("após voce terminar a missão, os moradores ficam agradecidos com sua conquista")
time.sleep(2)
print("o mesmo guarda vai até voce e fala: parabens por completar a missão, isso é tudo que voce tem para fazer por hoje")
time.sleep(1)




#fim do capitulo 1 e inicio o capitulo 2 ➡️

print('após voce voltar a vila, voce pensa em 3 opções, 1-voltar para sua casa na vila 2-ir para o ferreiro 3-ir para a biblioteca da cidade')

escolha2 = int(input())


#segundo treino - capitulo 2 📖
if escolha2 == 1:
    print('voce volta para sua casa')

if escolha2 == 2:
    print('voce melhorou suas habilidades em combate')
    combate+=3
    print(' seu combate: ', combate)
    print(combate)
if escolha2 == 3:
    print('voce melhorou sua magia')
    magia+=3
    print('sua magia: ', magia)

print('voce volta para sua casa depois de um longo dia')
time.sleep(3)
#loja - capitulo 2 🏪
print('voce acorda em um novo dia, e ao sair de sua casa, voce vai até a loja da cidade')
print('ao chegar na loja, o vendedor pede para voce escolher entre estes produtos')
print('poção de regeneração (50 moedas)')
print('adaga de prata (577 moedas)')
print('arco e flecha (495 moedas)')
print('flecha (10 moedas)')
compra = input()

if compra == 'poção de regeneração' and moedas_de_ouro >= 50:
    moedas_de_ouro -= 50
    print('voce agora tem uma poção de regeneração')
    print('moedas de ouro: ', moedas_de_ouro)
elif compra == 'arco e flecha' and moedas_de_ouro >= 495:
    moedas_de_ouro -= 495
    print('agora voce tem arco e flecha ')
    print('suas moedas de ouro: ', moedas_de_ouro)
elif compra == 'flecha' and moedas_de_ouro >= 10:
    moedas_de_ouro -= 10
    print('agora voce tem flecha')
    print('suas moedas de ouro: ', moedas_de_ouro)
elif compra == 'adaga de prata' and moedas_de_ouro >= 577:
    moedas_de_ouro -= 577
    print('agora voce tem uma adaga de prata')
    print('suas moedas de ouro: ', moedas_de_ouro)
else:
    print('voce não tem dinheiro suficiente para comprar esse item ou digitou algo errado')

