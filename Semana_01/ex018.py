# Faça um programa que leia um ângulo qualquer e mostre na tela o
# valor do seno, cosseno e tangente desse ângulo
# ver biblioteca Math
from math import sin, cos, tan, radians
print('=== DIGITE VALOR DO ANGULO E DAREMOS O SENO, COSSENO E TANGENTE ===')
angulo = float(input('Digite o valor do angulo: '))
seno = sin(radians(angulo))
coseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'Dado o ângulo {angulo}º, temos:'
      f'\nSeno = {seno:.2f}'
      f'\nCoseno = {coseno:.2f}'
      f'\nTangente = {tangente:.2f}')
