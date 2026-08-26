import os
import shutil 

pasta_de_origem = "C:/Users/gaido/downloads"
pasta_destino = {".iso": "ISOS", 
             ".rmskin" : "Skins rainmetter"
            }

for arquivo in os.listdir(pasta_de_origem):
    caminho_completo = os.path.join(pasta_de_origem, arquivo)
    if os.path.isfile(caminho_completo):
        _, extensao = os.path.splitext(arquivo)
        pasta = pasta_destino.get(extensao.lower())
        if pasta:
            destino = os.path.join(pasta_de_origem, pasta)
            os.makedirs(destino, exist_ok=True)
            shutil.move(caminho_completo, os.path.join(destino, arquivo))
            print("movido: {arquivo} → {pasta}")
