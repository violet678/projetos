print('gerador de senhas')
import random
import string
while True:
    def gerar_senha(tamanho=12):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        return senha

    # Exemplo de uso
    tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
    senha_gerada = gerar_senha(tamanho_senha)
    print(f"Sua senha gerada: {senha_gerada}")