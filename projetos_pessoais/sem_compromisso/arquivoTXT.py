texto = ' '
while texto != 'fim':
    texto = str(input('\nEscreva algo: ["fim" para sair]: '))
    if texto == 'fim':
        arquivo = open('arquivo.txt', 'a')
        arquivo.write('\n' + '#'*15 + '\n')
        arquivo.close()
        print('\tTexto não adicionado.')
        break
    else:
        arquivo = open('arquivo.txt', 'a')
        arquivo.write('\n' + texto + '\n')
        print('Texto adicionado com sucesso.')
        print(f'{texto}')
        arquivo.close()
print('F I M')
