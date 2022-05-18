from os import system

system('clear')
print('''
        Calculadora

    Escolha um cálculo:\n
    1 => Soma
    2 => Subtração
    3 => Multiplicação
    4 => Divisão
    5 => Potenciação
''')

while True:
    opcao = int(input('\nOpção: '))
    if opcao == 1:
        def code_sum(a, b):
            return a + b
        val_one = float(input('Number One: '))
        val_two = float(input('Number Two: '))
        resp = code_sum(val_one, val_two)
        system('clear')
        print(f'Soma: {resp}')
    elif opcao == 2:
        def code_sub(a, b):
            return a - b
        val_one = float(input('Number One: '))
        val_two = float(input('Number Two: '))
        resp = code_sub(val_one, val_two)
        system('clear')
        print(f'Subtração: {resp}')
    elif opcao == 3:
        def code_mult(a, b):
            return a * b
        val_one = float(input('Number One: '))
        val_two = float(input('Number Two: '))
        resp = code_mult(val_one, val_two)
        system('clear')
        print(f'Multiplicação: {resp}')
    elif opcao == 4:
        def code_div(a, b):
            return a / b
        val_one = float(input('Number One: '))
        val_two = float(input('Number Two: '))
        resp = code_div(val_one, val_two)
        system('clear')
        print(f'Divisão: {resp}')
    elif opcao == 5:
        def code_pot(a, b):
            return a ** b
        val_one = float(input('Number One: '))
        val_two = float(input('Number Two: '))
        resp = code_pot(val_one, val_two)
        system('clear')
        print(f'Potenciação: {resp}')
