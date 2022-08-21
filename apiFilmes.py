from distutils.cmd import Command
from tkinter import *
import requests
import json


class buscarFilmes:
    def __init__(self):
        self.janela = Tk()
        self.janela.title('Buscasr filmes')
        self.janela.geometry("500x400")
        self.janela.resizable(0,0)

        self.frameBusca = Frame(self.janela)
        self.frameBusca.pack()

        self.campoPesquisa = Entry(self.frameBusca, font="Arial 20 bold", width=20)
        self.campoPesquisa.pack()

        self.botaoPesquisar = Button(self.frameBusca, font="Arial 20", text="Buscar", width=5, command=self.pesquisarFilme())
        self.botaoPesquisar.pack()

        self.listarFilmes = Listbox(self.janela)
        self.listarFilmes.pack(fill=BOTH, expand=YES)
        #self.compoPesquisa.grid(row=0, column=0)
        self.janela.mainloop()
    

    def pesquisarFilme(self):
        try:
            requisicao = requests.get("http://www.omdbapi.com/?t=" + self.campoPesquisa.get()+"&apikey=88fc3206")
            dictFilmes = json.loads(requisicao.text)
            self.listarFilmes.delete(0, END)
            self.listarFilmes.insert(END, ('Nome do filme:' + dictFilmes['Title']))
            self.listarFilmes.insert(END, ('Ano do filme'+ dictFilmes['Year']))
        except:
            self.listarFilmes.delete(0, END)
            self.listarFilmes.insert(END, 'O filme não foi encontrado!!!')
            
buscarFilmes()
