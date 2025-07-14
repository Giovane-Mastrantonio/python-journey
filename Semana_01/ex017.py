# Faça um programa que leia o comprimento do cateto oposto e
# do cateto adjacente de um triangulo retângulo, calcule
# e mostre o comprimento da hipotenusa
# ver modulo Math
from math import hypot
print('=== DIGITE OS CATETOS QUE INFORMAREMOS A HIPOTENUSA ===')
cateto1 = float(input('Digite o comprimento do cateto oposto: '))
cateto2 = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = hypot(cateto1, cateto2)
print(f'A hipotenusa é igual a {hipotenusa:.2f}')
