'''
1.1.SAÍDA SIMPLES
1.1.2 Etiqueta - Elabore um programa que, após limpar a tela, escreve seu nome completo na primeira linha, seu endereço na segunda, e o CEP e telefone na terceira.'''

import os

print()

nome = str(input('Nome completo: '))
endereco = str(input('Endereço: '))
cep = str(input('CEP: '))
telefone = str(input('Telefone: '))

os.system('clear')

print(f'Nome completo: {nome.upper()}\nEndereço: {endereco}\nCEP: {cep} - Telefone: {telefone}')


