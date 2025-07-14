# Crie um programa que leia o nome de uma cidade e diga
# se ela começa ou não com o nome "SANTO".
print('=== DIGITE UM NOME DE CIDADE BRASILEIRA===')
cidade = str(input('Digite o nome da cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')
