import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image

class software(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Cadastro de nome e email')
        self.geometry("600x600")
        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.contatc_var = tk.StringVar()
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.create_widgets()

    def create_widgets(self):

        #Buttons
        branco_button = ttk.Button(self, text='BRANCO')
        branco_button.grid(column=0, row=16)

        anular_button = ttk.Button(self, text='ANULAR')
        anular_button.grid(column=1, row=16)

        confirmar_button = ttk.Button(self, text='CONFIRMAR')
        confirmar_button.grid(column=2, row=16)

        lula_button = ttk.Button(self, text='13', command=self.lula).grid(column=0, row=17)
        bolsonaro_button = ttk.Button(self, text='22', command=self.bolsonaro).grid(column=2, row=17)

        #Entry

        ttk.Entry(self, takefocus=True).grid(column=1, row=3)

        #Label

        ttk.Label(self, takefocus=True, text='LABEL'). grid(column=1, row=2)
        #Img

        img_brasil = Image.open("brasil.png")
        photo = ImageTk.PhotoImage(img_brasil)
        self.imagem = Label(self, text="adicionando", image=photo)
        self.imagem.image = photo
        self.imagem.grid(column=1, row=15)

    def lula(self):

        img_candidato2 = Image.open("lula.jpg")
        photo = ImageTk.PhotoImage(img_candidato2)
        self.imagem = Label(self, text="adicionando", image=photo)
        self.imagem.image = photo
        self.imagem.grid(column=0, row=15)

    def bolsonaro(self):

        img_candidato1 = Image.open("bolsonaro.jpg")
        photo = ImageTk.PhotoImage(img_candidato1)
        self.imagem = Label(self, text="adicionando", image=photo)
        self.imagem.image = photo
        self.imagem.grid(column=2, row=15)


if __name__ == "__main__":
    app = software()
    app.mainloop()

