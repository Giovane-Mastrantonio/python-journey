# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
# relembrando: são divisíveis por um e ele mesmo
texto = 'DESCOBRINDO NÚMEROS PRIMOS'
print(f'{texto:=^50}')
numero = int(input('Digite um numero inteiro: '))
divisor = 0
for c in range(1, numero +1):
    if numero % c == 0:
        divisor += 1
print(f"O número {numero} é PRIMO." if divisor == 2 else f"O número {numero} NÃO é primo.")
