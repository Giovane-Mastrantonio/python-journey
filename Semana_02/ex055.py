# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
texto = 'TESTANDO PESOS CORPORAIS'
print(f'{texto:=^50}')
print('Informe na sequencia o PESO de 5 pessoas.')
listaDePesos = []
for c in range(1, 6):
    peso = float(input(f'Informe o peso da {c}ª pessoa em Kg: '))
    listaDePesos.append(peso) #ADICIONA NA LISTA DE PESOS

print(f'\nO maior peso informado é {max(listaDePesos)} Kg.'
      f'\nE o menor informado é {min(listaDePesos)} Kg.')
