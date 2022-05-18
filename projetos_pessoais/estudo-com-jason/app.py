import ativo as at
from time import sleep
from os import system
import json

info = json.loads(at.data)

def ativa():
  sleep(2)
  print()
  print(f"\033[31m{'':#^60}")
  print(f"{' ATIVA ':#^60}")
  print(f"{'':#^60}")
  print()
  sleep(3)
  system('clear')
  for i in info:
      for k, v in i.items():
        sleep(.05)
        print(f'\t\033[93m{k}\033[m, \033[92m\033[1m{v}\033[m\033[m')
  print()

pergunta = input('\n\tExibir [s/n]: ')
if pergunta in 'sS':
  ativa()
elif pergunta in 'nN':
  print('\tENCERRADO')
else:
  print('\tBie Bie')