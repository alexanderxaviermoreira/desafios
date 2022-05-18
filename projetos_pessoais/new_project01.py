from rich import table
from rich.console import Console
from rich.table import Table
from time import sleep
from os import system

print()
table = Table(title='')
table.add_column('Cálculo do Imposto de Renda', justify='left', style='red', no_wrap=False)
table.add_row('''
    - Quem recebe até R$ 1.903, 98 é isento do tributo.
    - Entre R$ 1.903, 99 e R$ 2.826, 65, o imposto é de 7, 5 % .
    - Entre R$ 2.826, 66 e 3.751, 05, a taxa é de 15 % .
    - O tributo é de 22, 5 % para quem ganha entre R$ 3.751, 06 e R$ 4.664, 68.
''')
console = Console()
console.print(table)
print()
while True:
    salario_mensal = float(input('\tSalário Mensal: '))
    system('clear')
    rendimento_anual = salario_mensal * 12
    if salario_mensal > 0 and salario_mensal <= 1903.98:
        sleep(.5)
        print(f'Rendimento Anual: R$ {rendimento_anual:.2f}')
        print('\nContribuinte está ISENTO.\n')
    elif salario_mensal >= 1903.99 and salario_mensal <= 2826.65:
        sleep(.5)
        print(f'Rendimento Anual: R$ {rendimento_anual:.2f}')
        print('\nContribuinte pagará imposto de 7,5%.\n')
    elif salario_mensal >= 2826.66 and salario_mensal <= 3751.05:
        sleep(.5)
        print(f'Rendimento Anual: R$ {rendimento_anual:.2f}')
        print('\nContribuinte pagará imposto de 15%.\n')
    elif salario_mensal >= 3751.05 and salario_mensal <= 4664.68:
        sleep(.5)
        print(f'Rendimento Anual: R$ {rendimento_anual:.2f}')
        print('\nContribuinte pagará imposto de 22,5%.\n')
    elif salario_mensal >= 4664.69:
        sleep(.5)
        print(f'Rendimento Anual: R$ {rendimento_anual:.2f}')
        print('\nContribuinte pagará imposto de 27%.\n')
    elif salario_mensal <= 0:
        sleep(.5)
        print('\nENCERRADO\n')
        break
