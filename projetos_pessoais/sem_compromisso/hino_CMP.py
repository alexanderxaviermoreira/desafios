#!/usr/bin/env python3
import requests
from tkinter import *

app = Tk()

app.title('Canção do CMP - 2021')
#app.geometry('320x468')
cancao = Label(app, text='''
De Brasília irradiando ao Brasil
Teu exemplo de paz e labor,
Guarnecendo os destinos da Pátria,
Sem fraqueza com força e vigor.

Ocupando o cerrado da Pátria,
És o marco do herói pioneiro,
Onde a cruz do destino se faz,
No Planalto Central Brasileiro.

(Estribilho)
    Comando Militar do Planalto,
    Expressão de valor nacional,
    Teu porvir já se vê no presente,
    No visor do Planalto Central.

Teu destino é infinito e brilhante,
Pois semeias amor e progresso.
Na visão nacional brasileira
És o esteio da Pátria ao sucesso.

Vanguardeiro, na história moderna,
Sentinela da paz, altaneiro,
A distância vencendo com glória,
Em defesa do chão brasileiro.

(Estribilho)
    Comando Militar do Planalto,
    Expressão de valor nacional,
    Teu porvir já se vê no presente,
    No visor do Planalto Central.
	''')
cancao.grid(column='0', row='0', padx=5, pady=5)

app.mainloop()
