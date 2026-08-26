import os
import shutil

# Defina a pasta que deseja organizar
pasta_origem = "C:/Users/Victor/Downloads"  # Modifique conforme necessário

# Crie um dicionário com categorias e extensões
categorias = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Vídeos": [".mp4", ".avi", ".mov"],
    "Áudio": [".mp3", ".wav"],
    "Compactados": [".zip", ".rar"],
}

# Criar as pastas de destino caso não existam
for categoria in categorias.keys():
    pasta_destino = os.path.join(pasta_origem, categoria)
    os.makedirs(pasta_destino, exist_ok=True)

# Mover arquivos para suas respectivas categorias
for arquivo in os.listdir(pasta_origem):
    caminho_arquivo = os.path.join(pasta_origem, arquivo)
    if os.path.isfile(caminho_arquivo):  # Verifica se é um arquivo
        for categoria, extensoes in categorias.items():
            if any(arquivo.endswith(ext) for ext in extensoes):
                shutil.move(caminho_arquivo, os.path.join(pasta_origem, categoria))
                break

print("Organização concluída!")