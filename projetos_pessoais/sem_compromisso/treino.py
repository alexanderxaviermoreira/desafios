# def pet(tipo_animal, nome_animal):
#     print()
#     print(f'Meu {tipo_animal.title()} se chama {nome_animal.title()}.')
# pet('cachorro', 'luna')

# def new_pet(type_animal, name_animal):
#     print(f'\n{name_animal.title()} is the name of my {type_animal.title()}.')
# new_pet(type_animal='hamster', name_animal='harry')

# def familia(nome, parent='pai'):
#     print(f'{nome.title()} é o nome do meu {parent.title()}.')
# familia('alexander')

# def animal(raca, filo='cachorro'):
#     print(f'"{raca.title()}" é a raça do meu {filo.title()}.')
# animal('pastor')
# animal('pit bull')
# animal('labrador')
# animal('fila brasileira')

# def calc(x, y):
#     print()
#     x = int(input('Valor 01: '))
#     y = int(input('Valor 02: '))
#     print()
#     print(f'- Soma: {x+y}\n- Subtração: {x-y}\n- Multiplicação: {x*y}\n- Divisão: {x/y:.02f}')
#     print()
# calc('','')

# print()
# soma = 0
# notas = []
# acimaDaMedia = []
# abaixoDeSete = []
# nota = 0
# while nota != -1:
#     nota = float(input('Informe a nota: '))
#     if nota >= 0:
#         notas.append(nota)
#         soma += nota
#     else:
#         break
# print()
# print(f'Quantidade de notas: {len(notas)}')
# for nota in notas:
#     print(nota, end=' - ')
# print()
# notas.reverse()
# for nota in notas:
#     print(nota)
# print(f'Soma: {soma}')
# media = soma / len(notas)
# print(f'Média: {media}')
# for nota in notas:
#     if nota > media:
#         acimaDaMedia.append(nota)
# print(f'Quantidade de notas acima da média: {len(acimaDaMedia)}')
# for nota in notas:
#     if nota < 7:
#         abaixoDeSete.append(nota)
# print(f'Quantidade de notas abixo de 7: {len(abaixoDeSete)}')
# print('\nPrograma encerrado')

# palavra = 'montese'.upper()
# for letra in palavra:
#     print('_ ', end='')
# cj_Letras_Palavra = set(palavra)
# cj_Letras_Digitadas = set()
# erros = 0
# while (not cj_Letras_Palavra.issubset(cj_Letras_Digitadas)) and erros < 7:
#     print('\n')
#     letra_Digitada = input('Digite uma letra: ').upper()
#     cj_Letras_Digitadas.add(letra_Digitada)
#     if letra_Digitada in cj_Letras_Palavra:
#         print(f'A palavra é: ', end='')
#         for letra in palavra:
#             if letra in cj_Letras_Digitadas:
#                 print(f'{letra}', end='')
#             else:
#                 print(f'_ ', end='')
#     else:
#         erros += 1
#     print(f'\t\nErros: {erros} de 6.\nVamos jogar outra vez \U0001F923')
#     print(f'Letras já digitadas: \n', cj_Letras_Digitadas)
# if erros < 7:
#     print('Parabéns, você venceu.')
# else:
#     print('Infelizmente você perdeu')

# print()
# minha_lista = []
# while True:
#     cont_lista = input('Entre com dados: ')
#     minha_lista.append(cont_lista)
#     continuar = str(input('\tContinuar? [s/n]: '))
#     if continuar in 'sS' :
#         continue
#     elif continuar in 'nN':
#         print('Obrigado')
#         break
#     elif continuar not in 'sSnN':
#         print('Sim ou Não?')
#         continuar = str(input('\tContinuar? [s/n]: '))
#         continue
# for k, v in enumerate(minha_lista):
#     print(k+1, v.title())
# print(minha_lista)


# numeros = [1,2,3,4,5,6,7,8,9,10]
# pares = []
# for i in range(len(numeros)):
#     if numeros[i] % 2 == 0:
#         pares.append(numeros[i])
# print(pares)

# novos_nomes = ['marcos', 'pedro', 'joão']
# novo_nome = input('Novo nome: ')
# posicao = int(input('Posicao: '))
# novos_nomes.insert(posicao, novo_nome)
# print(novos_nomes)

# uma_lista = []
# uma_Tupla = ('alex', 'maria', 'gabriela', 'ana sofia')
# for nome in uma_Tupla:
#     uma_lista.append(nome)
# print(uma_lista)
# for k, v in enumerate(uma_Tupla):
#     print(k, v)
# print(uma_Tupla[0])
# print(uma_Tupla[1:])
# print(len(uma_Tupla))

from time import sleep
from os import system

hino = '''
\tDe Brasília irradiando ao Brasil
\tTeu exemplo de paz e labor,
\tGuarnecendo os destinos da Pátria,
\tSem fraqueza com força e vigor.

\tOcupando o cerrado da Pátria,
\tÉs o marco do herói pioneiro,
\tOnde a cruz do destino se faz,
\tNo Planalto Central Brasileiro.

\t(Estribilho)
\t\tComando Militar do Planalto,
\t\tExpressão de valor nacional,
\t\tTeu porvir já se vê no presente,
\t\tNo visor do Planalto Central.

\tTeu destino é infinito e brilhante,
\tPois semeias amor e progresso.
\tNa visão nacional brasileira
\tÉs o esteio da Pátria ao sucesso.

\tVanguardeiro, na história moderna,
\tSentinela da paz, altaneiro,
\tA distância vencendo com glória,
\tEm defesa do chão brasileiro.

\t(Estribilho)

\t\tComando Militar do Planalto,
\t\tExpressão de valor nacional,
\t\tTeu porvir já se vê no presente,
\t\tNo visor do Planalto Central.
'''
hino1 = list(hino)
while True:
    for l in hino1:
        sleep(.01)
        print(l, end = '', flush = True)
    sleep(3)
    system('clear')
