from tkinter import *
from webbrowser import BackgroundBrowser
import requests
import json

class tela_app:
    def __init__(self):
        self.dict = {}
        self.window = Tk()
        self.window.title('Dict')
        self.window.geometry('400x500')
        self.window.resizable(0,0)

        self.clima = Frame(self.window)
        self.clima.pack()

        api_clima = requests.get('https://weather.contrateumdev.com.br/api/weather/city/?city=Franca,Sãos%20Paulo')
        self.api = json.loads(api_clima.text)
        print(self.api)

        self.label2 = Label(self.clima,text=('C°'+ str(self.api['main']['temp'])), font='Arial 14 bold', width=56, height=2, bg='#483D8B', fg='black')
        self.label2.pack()
        #Tela1######################################
        self.tela_Conteúdo = Frame(self.window)
        self.tela_Conteúdo.pack()
        self.label = Label(self.tela_Conteúdo, font='Arial 15 bold', width=56, height=2, bg='#A9A9A9', fg='black')
        self.label.pack()

        #tela2######################################
        self.tela_dados = Frame(self.window)
        self.tela_dados.pack()

        self.label_chave = Label(self.tela_dados, text='Nome:',font='Impact 15 bold', width=8, height=2, bg='#00FF7F')
        self.label_chave.grid(row='0', column='0')
        self.label_valor = Label(self.tela_dados, text='Telefone:',font='Impact 15 bold', width=8, height=2, bg='#00FF7F')
        self.label_valor.grid(row='1', column='0')

        self.chave = Entry(self.tela_dados, font='Impact 24',width=47, bg='#98FB98', borderwidth=1)
        self.chave.grid(row=0, column=1)
        self.valor = Entry(self.tela_dados, font='Impact 24',width=47, bg='#98FB98', borderwidth=1)
        self.valor.grid(row=1, column=1)

        #tela3######################################

        self.tela_botoes = Frame(self.window)
        self.tela_botoes.pack()

        self.salvar = Button(self.tela_botoes, bg="#B0E0E6", bd=6, text="SALVAR", font='arial 10 bold', fg="red", width=11, height=1, command=lambda:self.salvar_def())
        self.salvar.grid(row=0, column=0)
        self.remover = Button(self.tela_botoes, bg="#B0E0E6", bd=6, text="REMOVER", font='arial 10 bold', fg="red", width=11, height=1, command=lambda:self.remover_def())
        self.remover.grid(row=0, column=1)
        self.modificar = Button(self.tela_botoes, bg="#B0E0E6", bd=6, text="MODIFICAR", font='arial 10 bold', fg="red", width=11, height=1, command=lambda:self.modificar_def())
        self.modificar.grid(row=0, column=2)


        #tela4######################################

        self.tela_lista = Frame(self.window)
        self.tela_lista.pack()

        self.lista = Listbox(self.tela_lista, font='Arial 20 bold')
        self.lista.pack(fill=BOTH, expand=YES)


        self.window.mainloop()

    
    def salvar_def(self):
        self.dict[self.chave.get()] = self.valor.get()
        self.lista.delete(0, END)
        for item, valor in self.dict.items():
            self.lista.insert(END, (f'{item} : {valor}'))
        self.label.configure(text= self.chave.get()+': '+ self.dict[self.chave.get()])

    
    def remover_def(self):
        del self.dict[self.chave.get()]
        self.lista.delete(0, END)
        for item, valor in self.dict.items():
            self.lista.insert(END, (f'{item} : {valor}'))
        self.chave.delete(0, END)
        self.valor.delete(0, END)
        self.label.configure(text='')


    def modificar_def(self):
        if self.chave.get() in self.dict:
            self.dict[self.chave.get()] = self.valor.get()
        else:
            self.dict[self.chave.get()] = self.valor.get()
        
        self.lista.delete(0, END)
        for item, valor in self.dict.items():
            self.lista.insert(END, (f'{item} : {valor}'))
        self.label.configure(text= self.chave.get()+': '+ self.dict[self.chave.get()])

tela_app()