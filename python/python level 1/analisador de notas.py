import time
print("bem vinda ao analisador de notas✏️📝  (≧∇≦)ﾉ")
while True:
    print("oque voce deseja fazer?")
    print("1 - calcular notas finais")
    print("2- adicionar notas")
    print("3- sair")
    escolha = int(input("digite o numero da opcao desejada: "))
    if escolha == 1:
        print("qual matéria voce quer calcular a nota?")
        print("1- artes")
        print("2- ciencias")
        print("3- geografia")
        print("4- historia")
        print("5- matematica")
        print("6- portugues")
        print("7- redação")
        materia = input("digite o numero da materia: ").strip().lower()
        if materia in ["artes", "1"]:
            notas = float(input("digite a soma das notas dos trabalhos: ").replace(",", "."))
            print(f"sua media final em artes é {notas}")
            if notas < 30:
                print("não passou, ficou de recuperação")
                time.sleep(5)
            else:
                print("parabens, voce passou")
                time.sleep(5)
        elif materia in ["ciencias", "2"]:
            notas = float(input("digite a soma das notas (provas + trabalho): ").replace(",", "."))
            print(f"sua media final em ciencias é {notas}")
            if notas < 30:
                print("não passou, ficou de recuperação")
                time.sleep(5)
            else:
                print("parabens, voce passou")
                time.sleep(5)
        elif materia in ["geografia", "3"]:
            notas = float(input("digite a soma das notas (provas + trabalho): ").replace(",", "."))
            print(f"sua media final em geografia é {notas}")
            if notas < 30:
                print("não passou, ficou de recuperação")
                time.sleep(5)
            else:
                print("parabens, voce passou")
                time.sleep(5)
        elif materia in ["historia", "4"]:
            notas = float(input("digite a soma das notas (provas + trabalho): ").replace(",", "."))
            print(f"sua media final em historia é {notas}")
            if notas < 30:
                print("não passou, ficou de recuperação")
                time.sleep(5)
            else:
                print("parabens, voce passou")
                time.sleep(5)
        elif materia in ["matematica", "5"]:
            notas = float(input("digite a soma das notas (provas + trabalho): ").replace(",", "."))
            print(f"sua media final em matematica é {notas}")
            if notas < 30:
                print("não passou, ficou de recuperação")
                time.sleep(5)
            else:
                print("parabens, voce passou")
                time.sleep(5)
        elif materia in ["portugues", "6"]:
            notas = float(input("digite a soma das notas (provas + trabalho): ").replace(",", "."))
            print(f"sua media final em portugues é {notas}")
            if notas < 30:
                print("não passou, ficou de recuperação")
                time.sleep(5)
            else:
                print("parabens, voce passou")
                time.sleep(5)
        elif materia in ["redação", "7"]:
            notas = float(input("digite a soma das notas: ").replace(",", "."))
            print(f"sua media final em redação é {notas}")
            if notas < 30:
                print("não passou, ficou de recuperação")
                time.sleep(5)
            else:
                print("parabens, voce passou")
                time.sleep(5)




    

