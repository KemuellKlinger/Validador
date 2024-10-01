from tkinter import *

class Buttones:
    def addBotao(self, info, func=None):
        self.button_func = func
        self.bb = Button(text=info, command=self.clickBotao)
        self.bb.pack()
        return self.bb
    
    def clickBotao(self):
        if self.button_func:
            self.button_func()
            