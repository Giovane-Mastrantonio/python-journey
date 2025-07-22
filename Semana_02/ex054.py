# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
# Considere maior idade com 21 anos
from datetime import date

texto = 'TESTANDO MAIORIDADE'
print(f'{texto:=^50}')
print('Informe na sequencia o ano de nascimento de 7 pessoas.')
anoAtual = date.today().year
menor = 0
maior = 0

for c in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    idade = anoAtual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print(f'\nAo todo existem {maior} pessoas MAIORES de idade.')
print(f'E existem {menor} pessoas MENORES de idade.')
