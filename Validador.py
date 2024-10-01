import re
import time
from tkinter import messagebox, ttk
from App import Janela as rt, Buttones as bt, Barra as br


class CriadorSenhaApp:
    def __init__(self):
        self.erros = 3
        self.key = ""
        self.iconBloqueio = "\U0001F512"
        self.iconInvalido = "\U0000274C"
        self.iconValidada = "\U00002705"
        self.iconTempo = "\U0000231B"
        self.incoSenhaValida = f"{self.iconBloqueio}{self.iconValidada}"
        
        self.janela = rt.Janela("Validador", 300, 100, "gray")
        self.butunn = bt.Buttones()
        self.entrada1 = self.janela.addEntrada("Crie sua senha")
        self.botao = self.butunn.addBotao("validar", lambda:self.verificar())

        self.janela.root.mainloop()

    def verificar(self):
        entrada = self.entrada1.get()
        self.key = entrada
        if len(entrada) > 8 and re.search(r'[A-Z]', entrada) and re.search(r'[a-z]', entrada) and re.search(r'\d', entrada) and re.search(r'[^a-zA-Z0-9\s]', entrada):
            messagebox.showinfo("Aviso", f"Senha Aceita!{self.incoSenhaValida}")
            self.validar_senha()
        else:
            messagebox.showwarning("Aviso", f"{self.iconInvalido}A senha deve conter no minimo: \n* 8 digitos \n* letras maiúsculas e minúsculas \n* números e caracteres especiais.")    

    def validar_senha(self):
        self.janela.destruir()
        self.novaJanela = rt.Janela("Validar Senha", 300, 100)
        self.butunn2 = bt.Buttones()
        entradaNJ = self.novaJanela.addEntrada("DIgite para validar")
        self.butunn2.addBotao("validar", lambda:verificarSenha())
        
        def verificarSenha():
            barrinha = br.Barra(self.novaJanela.root)
        
            if entradaNJ.get() == self.key:
                messagebox.showinfo("Aviso", f"Senha Validada com sucesso!{self.incoSenhaValida}")
                self.novaJanela.destruir()
            elif self.erros == 0:
                messagebox.showerror("Aviso", f"Senha Bloqueada!{self.iconBloqueio}")
                self.novaJanela.destruir()
            else:
                if self.erros == 3:
                    messagebox.showwarning("Aviso", f"Senha incorreta, sua Senha será bloqueada {self.iconBloqueio}: \nTentativas restantes: {self.erros}")
                else:
                    messagebox.showwarning("Aviso", f"Tentativas restantes: {self.erros}")
                self.erros -= 1

app = CriadorSenhaApp()
