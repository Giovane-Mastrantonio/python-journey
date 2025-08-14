# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o
# maior valor que estão na tupla.

from random import randint
texto = 'SORTEANDO NÚMEROS'
print(f'{texto:=^50}')
# Gerando 5 números aleatórios e colocando em uma tupla
numeros = (
    randint(0, 10),
    randint(0, 10),
    randint(0, 10),
    randint(0, 10),
    randint(0, 10)
)

# Mostrando a tupla gerada
print('Números sorteados:', end=' ')
for n in numeros:
    print(n, end=', ')

# Mostrando o maior e o menor valor
print(f'\nO maior valor sorteado foi {max(numeros)}.')
print(f'O menor valor sorteado foi {min(numeros)}.')
