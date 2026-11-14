# --bibliotecas--
import tkinter as tk
from tkinter import * 
from tkinter import ttk

class menu():
   
    def __init__(self):
        self.janela = tk.Tk()  # --janela principal do programa--
        app = self.janela   # -- chama a função da janela principal--
        app.title("Pomodoro App")
        app.geometry("400x300")  #tamanho da janela--
        
        p = ttk.Label(text="Pomodoro App", 
                      font=("Helvetica", 36)
                      )  # --escreve dentro da janela o nome do app--
        p.place(x=150, y=150)  # --posição do texto1 na janela--
        # -- controlando o tempo que quer estudar --
        self.label_txt = tk.Label(self.janela, 
                                  text="Minutos de foco:", 
                                  font=("Arial", 10)
                                  )
        self.label_txt.pack(pady=2)
        
        self.entrada_tempo = tk.Entry(self.janela, 
                                      font=("Arial", 12), 
                                      width=10
                                      )
        self.entrada_tempo.pack(pady=5)
        self.entrada_tempo.insert(0, "25")  # Valor padrão de 25 minutos

        # -- Mostrando o tempo na tela --
        self.label_tempo = tk.Label(self.janela, 
                                    text="25:00", 
                                    font=("Courier New", 32, "bold"))
        self.label_tempo.pack(pady=15)

        # -- Botão para iniciar --
        self.button = tk.Button(self.janela, text="Iniciar Pomodoro", 
                                font=("Arial", 12, "bold"), 
                                command=self.iniciar_contagem)
        self.button.pack(pady=10)
        self.button.place(x=250, y=200)  # --posição do botão na janela--

        self.rodando = False
        self.janela.mainloop()

    # --iniciando--

    # -- definindo a função do tempo rodar no escolhido
    def iniciar_contagem(self):
        if not self.rodando:
            self.rodando = True
            # -- obtendo o valor digitado pelo usuário --
            valor_digitado = self.entrada_tempo.get()
            
            if valor_digitado.isdigit():
                self.tempo_restante = int(valor_digitado) * 60
            else:
                self.tempo_restante = 25 * 60
            self.atualizar_relogio()

    # -- atualizando relógio
    def atualizar_relogio(self):
        if self.rodando and self.tempo_restante > 0:
            mins, segs = divmod(self.tempo_restante, 60)
            tempo_formatado = f"{mins:02d}:{segs:02d}"

            self.label_tempo.config(text=tempo_formatado)
            self.tempo_restante -= 1

            self.janela.after(1000, self.atualizar_relogio)
        elif self.tempo_restante == 0:
            self.label_tempo.config(text = "00:00")
            self.rodando = False
            print("Tempo esgotado!")

    # -- interface do programa --

if __name__ ==  "__main__":
    menu()
