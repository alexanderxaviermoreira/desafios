import pandas as pd

projetos = pd.read_csv('projetos_001.csv')
for e, projeto in enumerate(projetos['mad libs generator']):
    print(f'{e+1}: {projeto.title()}')