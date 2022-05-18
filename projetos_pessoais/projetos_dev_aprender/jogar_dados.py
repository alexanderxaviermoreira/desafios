import random
import PySimpleGUI as sg

class SimuladorDoDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = '\nVocê gostaria de gerar um \nnovo valor para o dados? '
        # Layout
        self.layout = [
            [sg.Text('Simulador de Dados')],
            [sg.Button('SIM'), sg.Button('NÃO')]
        ]        
    def Iniciar(self):
        # Criar uma jabela
        self.janela = sg.Window('Simulador de Dados', Layout = self.layout)
        # Ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # Fazer alguma coisa com esses valores  
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.GerarValorDeDado()
            elif self.eventos == 'nao' or self.eventos == 'n':                    
                print('Agradecemos a sua participacao.')
            else:
                print('Favor digitar sim ou não.')
        except:
            print('Ocorreu um erro ao receber sua resposta.')
    def GerarValorDeDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))
simulador = SimuladorDoDado()
simulador.Iniciar()