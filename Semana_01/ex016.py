# Crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a sua porção inteira
# exemplo digite um número:6.127
# O numero 6.127 tem a parte inteira 6
# ver funções do modulo MATH

from math import floor,trunc
print('=== DIGITE NÚMERO REAL E MOSTRAREMOS A PORÇÃO INTEIRA ===')
n1 = float(input('Digite o valor em Real: '))
print(f'O número digitado foi {n1} e a parte inteira é {floor(n1)}')
print(f'O número digitado foi {n1} e a parte inteira é {trunc(n1)}')
print(f'O número digitado foi {n1} e a parte inteira é {int(n1)}')
