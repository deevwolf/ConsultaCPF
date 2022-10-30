#Um Simples Painel De Consultas Cpf By Wolf/Oliver. Por Favor, Leia a ReadaMe.txt

import os
import time
import csv
import requests
#SISTEMA DE CORES
R = '\033[31m'
P = '\033[35m'
B = '\033[34m'
Y = '\033[33m'
G = '\033[32m'
W = '\033[39m'

#SISTEMA_CARREGAMENTO
def loading():
  print(f"{Y}AGUARDE UM INSTANTE.")
  time.sleep(1)
  print(f"{Y}AGUARDE UM INSTANTE..")
  time.sleep(1)
  print(f"{Y}AGUARDE UM INSTANTE...")
  time.sleep(1)
  print(f"{G}CONSULTA REALIZADA COM SUCESSO!")
  time.sleep(1)
  
#Retornar Ao Menu?
def retornar_menu():
  print("Deseja Retornar Ao Menu? (y/n)")
  menu = input("> ")
  if menu == 'y':
    os.system('clear')
    os.system('python main.py')
    if menu == 'n':
      exit()
  

#Consulta CEP


  
  
  
  

def desenho():
  print(f'''{B}______________________________________________¶¶¶¶________¶¶
  ____________________________________________¶¶_¶¶¶_______¶¶
  _____¶¶¶¶¶¶¶¶_____¶¶___¶¶¶¶_______________¶¶___¶¶______¶¶
  ___¶¶¶______¶¶¶__¶¶¶__¶¶________________¶¶____¶¶¶_____¶¶
  ____________¶¶¶__¶¶_¶¶¶_______________¶¶______¶¶_____¶¶
  ___¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶____¶¶¶¶¶¶¶¶¶__¶¶_______¶¶¶_____¶¶
  _¶¶¶¶______¶¶¶__¶¶_¶¶¶___¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶
  ¶¶¶_______¶¶¶__¶¶¶__¶¶¶_____________________¶¶¶_____¶¶
  ¶¶¶¶____¶¶¶¶¶__¶¶____¶¶¶____________________¶¶_____¶¶
  _¶¶¶¶¶¶¶¶_¶¶¶__¶¶_____¶¶____________________¶¶_____¶¶
  ______________________________________________________¶¶__
  ________________________________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
  _______________________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__
  ________________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____________
  __________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________________
  _________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______________________
  ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________________________
  ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶_¶¶¶¶¶¶¶¶_________________________
  ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶___¶__¶¶¶¶¶¶________________________
  _¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶___¶¶¶¶¶¶_______________________
  __¶¶¶¶¶¶¶¶¶______¶¶¶¶¶_______¶¶¶¶¶¶¶______________________
  ___¶¶¶¶¶¶________¶¶¶¶¶_________¶¶¶¶¶¶¶____________________
  ____¶¶¶¶_________¶¶¶¶¶__________¶¶¶¶¶¶¶¶__________________''')
desenho()
print("")
print(f"{B}##################################")
print(f"{W}Bem Vindo Ao Meu Script, Escolha Uma Opção Abaixo :")
print(f"{B}01{W} - CONSULTA CPF SIMPLES")
print(f"{B}02{W} - MEU GITHUB")
print(f"{B}##################################")
print("")
r = input("➤ ")
if r == '02':
  os.system("xdg-open https://github.com/deevwolf")
if r == '01':
  arquivo = csv.reader(open('db_cpf.csv') , delimiter='|')
  os.system('clear')
  desenho()
  print("")
  cpf = input("Informe O CPF :")
  for c in arquivo:
    if c[0] == cpf:
      loading()
      os.system('clear')
      desenho()
      print("")
      print(f'''
CONSULTA REALIZADA COM SUCESSO!
CPF: {c[0]}
NOME: {c[1]}
SEXO : {c[2]}
NASCIMENTO : {c[3]}

      
©WOLFOFC''')
      break
else:
  print("Não Encontrado.")
