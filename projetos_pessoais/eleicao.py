import os
votacao = []
dados = {}

while True:
    os.system('clear')
    dados['Número'] = int(input('\nNúmero do Candidato: '))
    if dados['Número'] == 17:
        dados['Nome do candidato'] = 'Jair Messias Bolsonaro'
    elif dados['Número'] == 13:
        dados['Nome do candidato'] = 'Luladrão'
    elif dados['Número'] != 13 or dados['Número'] != 17:
        dados['Nome do candidato'] = ''

    votacao.append(dados.copy())
    continuar = input('Continuar [s/n]: ')
    if continuar in 'sS':
        os.system('clear')
        continue
    elif continuar in 'nN':
        print('Votação Encerrada')
        os.system('clear')
        break


for v in votacao:
    for k, v in v.items():
        print(f'{k}: {v}')