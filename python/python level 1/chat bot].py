lista = []
import time
import random

while True:
    print('\n' + '-'*30)  # Separador visual
    print('Bem-vindo ao Charades! q(≧▽≦q)')
    print('O que gostaria de fazer?')
    print('1- Adicionar item à lista')
    print('2- Ver itens da lista')
    print('3- Remover item da lista')
    print('4- Sortear ação aleatória')
    print('5- Sair do programa')

    escolha = input('\nDigite o número aqui: ')

    # Opção 1: Adicionar item
    if escolha == '1':
        adicionar = input('O que você deseja adicionar? ')
        lista.append(adicionar)
        print(f'Item adicionado: "{adicionar}"')
        print(f'Lista atual: {lista}')

    # Opção 2: Ver lista
    elif escolha == '2':
        if not lista:
            print('A lista está vazia!')
        else:
            print('\nItens na lista:')
            for indice, item in enumerate(lista):
                print(f'{indice}: {item}')

    # Opção 3: Remover item
    elif escolha == '3':
        if not lista:
            print('A lista está vazia!')
        else:
            print(f'Itens atuais: {lista}')
            try:
                item_removido = input('Qual item você quer remover? (digite o nome ou índice): ')
                # Tenta remover por índice (se digitou um número)
                if item_removido.isdigit():
                    item_removido = int(item_removido)
                    if 0 <= item_removido < len(lista):
                        removido = lista.pop(item_removido)
                        print(f'Item removido (por índice): "{removido}"')
                    else:
                        print('Índice inválido!')
                # Remove por nome (se digitou texto)
                elif item_removido in lista:
                    lista.remove(item_removido)
                    print(f'Item removido (por nome): "{item_removido}"')
                else:
                    print('Item não encontrado!')
                print(f'Lista atualizada: {lista}')
            except:
                print('Erro ao remover!')

    # Opção 4: Ação aleatória
    elif escolha == '4':
        if not lista:
            print('A lista está vazia! Adicione itens primeiro.')
        else:
            sorteado = random.choice(lista)
            print('\n' + '='*30)
            print(f'>>> Ação sorteada: "{sorteado}"! <<<')
            print('='*30 + '\n')
            time.sleep(2)  # Pausa dramática

    # Opção 5: Sair
    elif escolha == '5':
        print('Até mais! (＾▽＾)／')
        break

    # Tratamento de erro
    else:
        print('Opção inválida! Digite um número de 1 a 5.')