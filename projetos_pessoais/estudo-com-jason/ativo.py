import json
from os import system
from time import sleep

data = '''
[
  {
    "Posto Graduação": "Cap QAO-Adm G",
    "Nome": "ADRIANO DE LIMA VINDILINO (VINDILINO)",
    "OM": "4º BE Cmb (Itajubá-MG)",
    "E-mail": "vindilino90@gmail.com"
  },
  {
    "Posto Graduação": "Cap QAO-Adm G",
    "Nome": "ANTONIO EZEQUIEL DE SOUSA BARROS (EZEQUIEL)",
    "OM": "DPGO (Brasília-DF)",
    "E-mail": "ezequieldct@gmail.com"
  },
  {
    "Posto Graduação": "Cap QAO-Adm G",
    "Nome": "CÉSAR RICARDO VELASQUE TRINDADE (VELASQUE)",
    "OM": "Cmdo 9ª RM (Campo Grande-MS)",
    "E-mail": "crvtrindade@gmail.com"
  },
  {
    "Posto Graduação": "Cap QAO-Adm G",
    "Nome": "CLAUDIO RENIS DA SILVA (RENIS)",
    "OM": "4º BEC (Barreiras-BA)",
    "E-mail": "claudiorenis@gmail.com"
  },
  {
    "Posto Graduação": "Cap QAO-Adm G",
    "Nome": "DARCÍLIO CARVALHO SANTANA (DARCILIO)",
    "OM": "SEF (Brasília-DF)",
    "E-mail": "darciliosantana@gmail.com"
  },
  {
    "Posto Graduação": "Cap QAO-Adm G",
    "Nome": "EDVAR TIMBÓ MENDES SOBRINHO (EDVAR)",
    "OM": "59º BI Mtz (Maceió-AL)",
    "E-mail": "edvar_4022@hotmail.com"
  },
  {
    "Posto Graduação": "Cap QAO-Adm G",
    "Nome": "FLAVIO FREDERICO (FREDERICO)",
    "OM": "CMRJ (Rio de Janeiro-RJ)",
    "E-mail": "flaviofredy@hotmail.com"
  },
  {
    "Posto Graduação": "Cap QAO-Adm G",
    "Nome": "FRANCISCO JOSÉ DOS SANTOS (DOS SANTOS)",
    "OM": "Cmdo 6ª RM (Salvador-BA)",
    "E-mail": "dossantos.montese90@gmail.com"
  },
  {
    "Posto Graduação": "Cap QAO-Adm G",
    "Nome": "GIOVANI JADER DO NASCIMENTO (JADER)",
    "OM": "4º BE Cmb (Itajubá-MG)",
    "E-mail": "giovanijadernascimento@gmail.com"
  },
  {
    "Posto Graduação": "Cap QAO-Adm G",
    "Nome": "JOÃO BOSCO DOS SANTOS FERREIRA (BOSCO)",
    "OM": "COTER (Brasília-DF)",
    "E-mail": "jbsf70@gmail.com"
  },
  {
    "Posto Graduação": "Cap QAO-Adm G",
    "Nome": "JOÃO JUSTINO SANTOS DE MORAES (JUSTINO)",
    "OM": "Cmdo 1º Gpt E (João Pessoa-PB)",
    "E-mail": "jjustinosm@gmail.com"
  },
  {
    "Posto Graduação": "Cap QAO-Adm G",
    "Nome": "JOSIAS SILVA DE OLIVEIRA (JOSIAS)",
    "OM": "Cmdo 7ª RM (Recife-PE)",
    "E-mail": "stenjosias@gmail.com"
  },
  {
    "Posto Graduação": "Cap QAO-Adm G",
    "Nome": "JURANDIR SOARES VENTURA (VENTURA)",
    "OM": "Cmdo 7ª RM (Recife-PE)",
    "E-mail": "jurandirventura@gmail.com"
  },
  {
    "Posto Graduação": "Cap QAO-Adm G",
    "Nome": "KENNEDY MARCOS SOARES (KENNEDY)",
    "OM": "2º BEC (Teresina-PI)",
    "E-mail": "kmsoares681@gmail.com"
  },
  {
    "Posto Graduação": "Cap QAO-Adm G",
    "Nome": "LUÍS FLÁVIO FALCAO TORRES (FALCAO)",
    "OM": "Esqd Cmdo 1ª Bda C Mec (Santiago-RS)",
    "E-mail": "lfalcaotorres@gmail.com"
  },
  {
    "Posto Graduação": "Cap QAO-Adm G",
    "Nome": "MARCELO LUIZ DA SILVA (MARCELO LUIZ)",
    "OM": "CTEx (Rio de Janeiro-RJ)",
    "E-mail": "marcelofhp@gmail.com"
  },
  {
    "Posto Graduação": "Cap QAO-Adm G",
    "Nome": "MARCOS LIMA DOS SANTOS (LIMA SANTOS)",
    "OM": "Cia Cmdo 1º Gpt E (João Pessoa-PB)",
    "E-mail": "limapqdtsantos@hotmail.com"
  },
  {
    "Posto Graduação": "Cap QAO-Adm G",
    "Nome": "RENATO WISNIEWSKI (RENATO)",
    "OM": "4º B Log (Santa Maria-RS)",
    "E-mail": "ticuna2000@bol.com.br"
  },
  {
    "Posto Graduação": "Cap QAO-Adm G",
    "Nome": "RIVANILDO GOMES DOS SANTOS (GOMES)",
    "OM": "MD (Brasília-DF)",
    "E-mail": "gomesrgs@gmail.com"
  },
  {
    "Posto Graduação": "Cap QAO-Adm G",
    "Nome": "SILVIO SALES DE MENDONÇA (SILVIO)",
    "OM": "D M E (Brasília-DF)",
    "E-mail": "silviosalesmendonca@gmail.com"
  },
  {
    "Posto Graduação": "1º Ten QAO-Adm G",
    "Nome": "FLAVIO BARBOSA AMORIM (FLÁVIO AMORIM)",
    "OM": "BCSv/AMAN (Resende-RJ)",
    "E-mail": "amorim_flavio@yahoo.com.br"
  },
  {
    "Posto Graduação": "1º Ten QAO-Adm G",
    "Nome": "GIOVANI PRADO DE FARIA (GIOVANI)",
    "OM": "14º GAC (Pouso Alegre-MG)",
    "E-mail": "giovaniprado1968@gmail.com"
  },
  {
    "Posto Graduação": "1º Ten QAO-Adm G",
    "Nome": "JORGE LUIS GARCIA D ANGELO (D ANGELO)",
    "OM": "Cia Cmdo CML (Rio de Janeiro-RJ)",
    "E-mail": "dangelo_1969@yahoo.com.br"
  },
  {
    "Posto Graduação": "1º Ten QAO-Adm G",
    "Nome": "PAULO AIRTON ALMEIDA CARVALHO (CARVALHO)",
    "OM": "H Gu ALEGRETE (Alegrete-RS)",
    "E-mail": "paulo_airton90@yahoo.com.br"
  },
  {
    "Posto Graduação": "1º Ten QAO-Adm G",
    "Nome": "PAULO HENRIQUE SOARES FONTES (HENRIQUE)",
    "OM": "Cmdo 1ª RM (Rio de Janeiro-RJ)",
    "E-mail": "phsfontes68@gmail.com"
  },
  {
    "Posto Graduação": "2º Ten QAO-Adm G",
    "Nome": "MANOEL ALVES TEIXEIRA (ALVES)",
    "OM": "DPIMA (Brasília-DF)",
    "E-mail": "alvinho758@hotmail.com"
  },
  {
    "Posto Graduação": "S Ten Eng",
    "Nome": "ALEXANDER XAVIER MOREIRA (ALEXANDER)",
    "OM": "CRO / 11ª RM (Brasília-DF)",
    "E-mail": "alexkurumin@gmail.com"
  },
  {
    "Posto Graduação": "S Ten Eng",
    "Nome": "ALFEU BRANDÃO SILVA (BRANDÃO)",
    "OM": "9º BEC (Cuiabá-MT)",
    "E-mail": "alfeubrandao@gmail.com"
  },
  {
    "Posto Graduação": "S Ten Eng",
    "Nome": "MARCOS PINTO DE OLIVEIRA FRANÇA (MARCOS PINTO)",
    "OM": "25º B Log (Es) (Rio de Janeiro-RJ)",
    "E-mail": "naviotanque055@gmail.com"
  }
]
'''

info = json.loads(data)

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