from tkinter import * 
from tkinter import ttk
import time

class Barra:
    def __init__(self, master):
        self.varBarra = DoubleVar()
        self.varBarra.set(0)
        self.progresso = ttk.Progressbar(variable=self.varBarra, maximum=100)
        self.progresso.pack()
        self.atualizarBarra(master)
        self.progresso.destroy()
        
    def atualizarBarra(self, master):
        cont = 0
        etapas = 10000 / 100
        while cont < etapas:
            cont += 1
            self.varBarra.set(cont)
            master.update()
            time.sleep(0.02)
        
        
# Como usar       
# barrinha = Barra(nomeDaJanela.root)
