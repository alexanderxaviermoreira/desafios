from time import sleep
import os

while True:
    def anoPassado(year):
        return f'\nO ano de {year} foi duro e nós crescemos\n'
    resposta = anoPassado('2021')
    os.system('clear')
    sleep(2)    
    print(resposta)
    sleep(2)
    os.system('clear')

    def anoNovo(newYear):
        return f'\nSe {newYear} for um ano difícil também cresceremos\n'
    novaResposta = anoNovo('2022')
    sleep(2)
    print(novaResposta)
    sleep(2)
    os.system('clear')
