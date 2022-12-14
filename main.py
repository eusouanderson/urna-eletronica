import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import dialog

class software(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Eleições 2022')
        self.geometry("600x600")
        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.contatc_var = tk.StringVar()
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.create_widgets()


    def create_widgets(self):

        branco_button = ttk.Button(self, text='BRANCO')
        branco_button.grid(column=0, row=16)

        anular_button = ttk.Button(self, text='ANULAR')
        anular_button.grid(column=1, row=16)

        lula_button = ttk.Button(self, text='13', command=self.lula).grid(column=0, row=17)
        bolsonaro_button = ttk.Button(self, text='22', command=self.bolsonaro).grid(column=2, row=17)

        img_brasil = Image.open("brasil.png")
        photo = ImageTk.PhotoImage(img_brasil)
        self.imagem = Label(self, text="adicionando", image=photo)
        self.imagem.image = photo
        self.imagem.grid(column=1, row=15)

    def lula(self):

        self.img_candidato2 = Image.open("lula.jpg")
        photo = ImageTk.PhotoImage(self.img_candidato2)
        self.imagem = Label(self, text="adicionando", image=photo)
        self.imagem.image = photo
        self.imagem.grid(column=2, row=15)
        self.buttons()
        #Label
        ttk.Label(self, takefocus=True, text=f'{lulasobre}').grid(column=1, row=2)
        def confirmarlula():
            ttk.Label(self, takefocus=True, text='Você Votou no Candidato Lula').grid(column=1, row=2)

    def bolsonaro(self):

        self.img_candidato1 = Image.open("bolsonaro.jpg")
        photo = ImageTk.PhotoImage(self.img_candidato1)
        self.imagem = Label(self, text="adicionando", image=photo)
        self.imagem.image = photo
        self.imagem.grid(column=2, row=15)
        self.buttons()
        bosonaroframe = Frame().grid(column=0)
        ttk.Label(bosonaroframe, takefocus=True, text=f'{bolsonarosobre}').grid(column=1, row=2)
        def confirmarbolsonaro(self):
            ttk.Label(self, takefocus=True, text='Você Votou no Candidato Jair Bolsonaro').grid(column=1, row=2)

    def buttons(self, opc):
        if opc == 1:
            confirmar_button = ttk.Button(self, text='CONFIRMAR', command=...)
            dialog.showinfo()
        if opc == 2:
            confirmar_button.grid(column=2, row=16)


lulasobre = ('''Sobre
Luiz Inácio Lula da Silva, mais conhecido como Lula, é um ex-metalúrgico,
ex-sindicalista e político brasileiro. Filiado ao Partido dos Trabalhadores, 
foi o 35.º presidente do Brasil entre 1.º de janeiro de 2003 e 1.º de janeiro de 2011. Wikipédia
Nascimento: 27 de outubro de 1945 (idade 77 anos), Caetés, Pernambuco
Cônjuge: Rosângela Lula da Silva (desde 2022), MAIS
Filhos: Fábio Luís Lula da Silva, Sandro Luís, Luís Cláudio, Marcos Cláudio Lula da Silva, 
Lurian Cordeiro Lula da Silva
Mandato presidencial: 1 de janeiro de 2003 – 1 de janeiro de 2011
Nome completo: Luiz Inácio Lula da Silva
Partido: Partido dos Trabalhadores''')

bolsonarosobre = ('''Sobre
Jair Messias Bolsonaro GOMM é um militar reformado e político brasileiro, 
atualmente filiado ao Partido Liberal. É o 38.º presidente do Brasil desde 
1.º de janeiro de 2019, tendo sido eleito pelo Partido Social Liberal. 
Foi deputado federal pelo Rio de Janeiro entre 1991 e 2018. Wikipédia
Nascimento: 21 de março de 1955 (idade 67 anos), Glicério, São Paulo
Cônjuge: Michelle Bolsonaro (desde 2007), Rogéria Bolsonaro (de 1978 a 1997)
Filhos: Eduardo Bolsonaro, Laura Bolsonaro, Flávio Bolsonaro, Carlos Bolsonaro, Renan Bolsonaro
Nome completo: Jair Messias Bolsonaro
Mandato presidencial: 1 de janeiro de 2019 –
Cargo: Presidente do Brasil desde 2019
Partido: Partido Liberal''')

if __name__ == "__main__":
    app = software()
    app.mainloop()

