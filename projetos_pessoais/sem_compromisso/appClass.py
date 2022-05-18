class Militar:
    '''Informações de um Militar'''
    def __init__(self, postoGrad, nomeGuerra, funcao):
        self.postoGrad = postoGrad
        self.nomeGuerra = nomeGuerra
        self.funcao = funcao

posto_grad_militar = input('Posto/Grad: ')
nome_do_militar = input('Nome: ')
funcao_militar = input('Função: ')
militar01 = Militar(posto_grad_militar, nome_do_militar, funcao_militar)
print(f"\n\tPosto/Grad: {militar01.postoGrad.upper()}\n\tNome de Guerra: {militar01.nomeGuerra.title()}\n\tFunção: {militar01.funcao.title()}")


class calcCubo():
    def __init__(self, valor):
        self.x = valor
    def calcula_cubo(self):
        cubo = pow(self.x, 3)
        return f'Cubo do valor: {cubo}'

numero = int(input('Valor: '))
teste = calcCubo(numero)
resp = teste.calcula_cubo()
print(resp)

class Cubo:
    def __init__(self, valor):
        self.x = valor
    def calcula_cubo(self):
        cubo = pow(self.x, 3)
        return f'Cubo: {cubo}'
while True:
    novo_valor = int(input('Valor: '))
    teste = Cubo(novo_valor)
    c = teste.calcula_cubo()
    print(c)


class Calculo:
    def __init__(self, valor):
        self.x = valor

novo_valor = int(input('Valor: '))
valor_cubo = Calculo(novo_valor)    
print(pow(novo_valor, 3))


