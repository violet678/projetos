# --bibliotecas--
import json
import time
import tkinter as tk
from tkinter import * 
from tkinter import ttk
from pathlib import Path
from datetime import datetime


# -- definições --
ARQUIVO_DADOS = "historico_estudos.json" #documento onde os dados estão salvos --






# carregando dados
def carregar_dados():
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


# salvando dados
def salvar_dados(dados):
    """Salva o dicionário com o histórico atualizado em disco."""
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f: # -- salva os dados em um arquivo--
        json.dump(dados, f, indent=4, ensure_ascii=False)




def iniciar_pomodoro(materia, minutos_foco=25):
    segundos = minutos_foco * 60 # --multiplica os segundos para converter em minutos--
    print(f"\n[Foco Iniciado] Matéria: {materia} | Duração: {minutos_foco} min") # --mostra o tempo--

    # --coloca  uma excessão q se acabar o tempo, o progeama acaba--
    try:
        while segundos > 0:
            mins, segs = divmod(segundos, 60)
            tempo_formatado = f"{mins:02d}:{segs:02d}"
            print(f"\rTempo restante: {tempo_formatado}", end="")
            time.sleep(1)
            segundos -= 1
        
        print("\n\n🎉 Ciclo de foco concluído com sucesso!") # -- ciclo terminado com sucesso--
        
        # Atualiza o histórico
        dados = carregar_dados()
        hoje = datetime.now().strftime("%Y-%m-%d")
        
        if hoje not in dados:
            dados[hoje] = {}
        
        dados[hoje][materia] = dados[hoje].get(materia, 0) + minutos_foco 
        salvar_dados(dados)
        print(f"Sua sessão foi salva com sucesso no histórico de hoje ({hoje})!") # -- fala que a matéria foin salva--
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Ciclo interrompido antes do tempo.")

def exibir_estatisticas():
  # -- entrega um resumo do tempo estudando a matéria --
    dados = carregar_dados()
    if not dados:
        print("\nNenhum registro de estudo encontrado ainda.")
        return

    # -- estatisticas de tempo de estudo--
    print("\n=== ESTATÍSTICAS DE ESTUDO ===")
    for data, materias in dados.items():
        print(f"\n📅 Data: {data}")
        for materia, tempo in materias.items():
            horas = tempo / 60
            print(f"  • {materia}: {tempo} min (~{horas:.1f}h)")

def menu():
   # -- interface do programa --
    app = tk.Tk() # --diz para o app onde ele deve iniciar 
    app.title("Pomodoro App")
    app.geometry("400x300") #tamanho da janela--
    p = ttk.Label( text="Pomodoro App") # --escreve dentro da janela--
    p.place (x=150, y=10) # --posição do texto na janela--




    app.mainloop()
if __name__ == "__main__":
    menu()
