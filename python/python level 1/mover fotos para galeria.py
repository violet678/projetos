import os
import shutil

pasta_origem = "C:/Users/gaido/Downloads"
pasta_destino = "C:/Users/gaido/Pictures/Screenshots"

extensoes_para_mover = [".png", ".jpeg", ".jpg", ".jpeg", ".webp"]

for arquivo in os.listdir(pasta_origem):
    caminho_completo = os.path.join(pasta_origem, arquivo)
    if os.path.isfile(caminho_completo):
        _, extensao = os.path.splitext(arquivo)
        if extensao.lower() in extensoes_para_mover:
            destino_final = os.path.join(pasta_destino, arquivo)
            shutil.move(caminho_completo, destino_final)
            print(f"Movido: {arquivo} → C:/Users/gaido/Pictures/Screenshots")