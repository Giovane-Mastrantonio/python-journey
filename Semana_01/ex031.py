# Desenvolva um programa que pergunte a distancia de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$ 0.50 por Km para viagens de
# até 200 Km e R$ 0.45 para viagens mais longas
print('CALCULADORA DE PASSAGEM')
km = float(input('Qual a distância em Km: '))
# if km <= 200:
#     precopassagem = km * 0.50
#     print(f'O preço da passagem é R$ {precopassagem:.2f}')
# else:
#     precopassagem = km * 0.45
#     print(f'Acima de 200 Km o preço da passagem é R$ {precopassagem:.2f}')
preco = km * 0.50 if km <= 200 else km * 0.45
print(f'O preço da passagem é de R$ {preco:.2f}')
