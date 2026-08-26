#notas da escola
print("bem vinda ao contador de notas ✏️(≧∇≦)ﾉ")
while True:
    print("qual materia voce quer contabilizar as notas?")
    print("1 - artes")
    print("2 - ciencias")
    print("3 - matematica") 
    print("4 - historia")
    print("5 - geografia")      
    print("6 - portugues")
    print("7 - ingles") 
    print("8- redação")
    materia = input("digite a materia: ").upper().lower()
    #artes
    if materia in ["artes", "1"]:
        nota1 = float(input("digite a primeira nota: "))
        nota2 = float(input("digite a segunda nota: "))
        media = nota1 + nota2
        print(f"sua media final em artes é {media}")
        if media >= 30:
            print("parabens, voce passou em artes! (≧∇≦)ﾉ")
        else:
            print("voce ficou de recuperação em artes, estude mais! (╥﹏╥)")
    #ciencias
    elif materia in ["ciencias", "2"]:
        nota1 = float(input("digite a primeira nota: "))
        nota2 = float(input("digite a segunda nota: "))
        nota3 = float(input("digite a nota do trabalho (se tiver): "))
        media = (nota1 + nota2 + nota3) 
        print(f"sua media final em ciencias é {media}")
        if media >= 30:
            print("parabens, voce passou em ciencias! (≧∇≦)ﾉ")
        else:
            print("voce ficou de recuperação em ciencias, estude mais! (╥﹏╥)")
    #matematica
    elif materia in ["matematica", "3"]:
        nota1 = float(input("digite a primeira nota: "))
        nota2 = float(input("digite a segunda nota: "))
        nota3 = float(input("digite a nota do trabalho (se tiver): "))
        media = (nota1 + nota2 + nota3) 
        print(f"sua media final em matematica é {media}")
        if media >=30:
            print("parabens, voce passou em matematica! (≧∇≦)ﾉ")
        else:
            print("voce ficou de recuperação em matematica, estude mais! (╥﹏╥)")
    #historia
    elif materia in ["historia", "4"]:
        nota1 = float(input("digite a primeira nota: "))
        nota2 = float(input("digite a segunda nota: "))
        nota3 = float(input("digite a nota do trabalho (se tiver): "))
        media = (nota1 + nota2 + nota3)
        print(f"sua media final em historia é {media}")
        if media >=30:
            print("parabens, voce passou em historia! (≧∇≦)ﾉ")
        else:
            print("voce ficou de recuperação em historia, estude mais! (╥﹏╥)")
    #geografia 
    elif materia in ["geografia", "5"]:
        nota1 = float(input("digite a primeira nota: "))
        nota2 = float(input("digite a segunda nota: "))
        nota3 = float(input("digite a nota do trabalho (se tiver): "))
        media = (nota1 + nota2 +nota3)
        print(f"sua media final em geografia é {media}")
        if media >=30:
            print("parabens, voce passou em geografia! (≧∇≦)ﾉ")
        else:
            print("voce ficou de recuperação em geografia, estude mais! (╥﹏╥)")
    #portugues
    elif materia in ["portugues", "6"]:
        nota1 = float(input("digite a primeira nota: "))
        nota2 = float(input("digite a segunda nota: "))
        nota3 = float(input("digite a nota do trabalho (se tiver): "))
        media = (nota1 + nota2 +nota3)
        print(f"sua media final em portugues é {media}")
        if media >=30:
            print("parabens, voce passou em portugues! (≧∇≦)ﾉ")
        else:
            print("voce ficou de recuperação em portugues, estude mais! (╥﹏╥)")
    #ingles
    elif materia in ["ingles", "7"]:
        nota1 = float(input("digite a primeira nota: "))
        nota2 = float(input("digite a segunda nota: "))
        nota3 = float(input("digite a nota do trabalho (se tiver): "))
        media = (nota1+ nota2 + nota3)
        print(f"sua media final em ingles é {media}")
        if media >=30:
            print("parabens, voce passou em ingles! (≧∇≦)ﾉ")
        else:
            print("voce ficou de recuperação em ingles, estude mais! (╥﹏╥)")
    #redação
    elif materia in ["redação", "8"]:
        nota1 = float(input("digite a primeira nota: "))
        nota2 = float(input("digite a segunda nota: "))
        media = (nota1 + nota2)
        print(f"sua media final em redação é {media}")
        if media >=30:
            print("parabens, voce passou em redação! (≧∇≦)ﾉ")
        else:
            print("voce ficou de recuperação em redação, estude mais! (╥﹏╥)")
