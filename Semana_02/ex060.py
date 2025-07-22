# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Fatorial de exemplo: 5!=5x4x3x2x1=120
from math import factorial
texto = 'CALCULO DE FATORIAL'
print(f'{texto:=^50}')
# print('Utilizando o factorial do pacote Math no Python')
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print(f'O factorial de {n} é igual a {f}')
print('---FIM---')

# ===> Abaixo solução com resolução clássica
# n = int(input("Digite um número inteiro: "))
# fatorial = 1
# print(f"{n}! = ", end="")
# # loop para calcular o fatorial
# for i in range(n, 0, -1):
#     fatorial *= i
#     # imprime cada passo da multiplicação
#     if i > 1:
#         print(f"{i} x ", end="")
#     else:
#         print(f"{i} = ", end="")
#
# print(f"{fatorial}")
