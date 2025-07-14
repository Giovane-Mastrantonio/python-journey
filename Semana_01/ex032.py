# Faça um programa que leia um ano qualquer e
# mostre se ele é BISSEXTO
# date.today().year pega o ano atual da máquina rodada e depende
# da importação => from datetime import date
import calendar

print('DIZ SE UM ANO É BISSEXTO')
ano = int(input('Digite um ano qualquer: '))
if calendar.isleap(ano):
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} NÃO é BISSEXTO!')

#MATEMATICAMENTE DARIA PARA FAZER ASSIM
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} NÃO é BISSEXTO!')
