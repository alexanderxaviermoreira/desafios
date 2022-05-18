#!/usr/bin/env python3
import requests
import os
import random
from tkinter import *

def ronda():    
    from time import sleep
    horarios = ['20:00', '20:05', '20:10', '20:15', '20:20', '20:25', '20:30',
                '20:35', '20:40', '20:45', '20:50', '20:55', '21:00']
    print()
    os.system('clear')
    print('#'*36)
    print('{:^36}'.format('OS HORÁRIOS DA RONDA DEFINIDOS \nPOR "SORTEIO ELETRÔNICO'))
    print('#'*36)
    print()
    res = (random.shuffle(horarios))
    for k, h in enumerate(horarios):
        sleep(.5)
        print(f'\t{k + 1} - Horário: \033[31m{h}\033[0;0m')
    print()
    print('{:^36}'.format('\033[32mLIMITE: ATÉ 21:00 H\033[0m'))
    print()
    
    texto_gerar['text']
    
janela = Tk()
janela.title('Horários de Ronda')
janela.geometry('360x568')
texto_orientacao = Label(janela, text='Clique no botão para gerar os Horários de Ronda.')
texto_orientacao.grid(column=0, row=0, padx=20, pady=20)

botao = Button(janela, text='GERAR RONDA', command=ronda)
botao.grid(column=0, row=1, padx=20, pady=20)

texto_gerar = Label(janela, text='')
texto_gerar.grid(column=0, row=2, padx=20, pady=20)

janela.mainloop()
