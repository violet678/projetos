livro = {}
print('🌟🌟🌟 estante de livros🌟🌟🌟')
while True:
    print('oque desejeza fazer?')
    print('1-ver catalogo')
    print('2-adicionar livro a estante')
 

    escolha =  int(input())


    if escolha == 1:
        print('seus livros')
        print(livro)
    
    if escolha == 2:
        name = input('qual o nome do livro que voce quer adicionar?')
        autor = input('qual o nome do autor do livro? ')
        livro[name] = autor
        print('estante atualizada!')
  
