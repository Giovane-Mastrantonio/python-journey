# Faça um programa que leia três números e mostre qual é o maior
# e qual é o menor.
print('QUAL O MAIOR E MENOR NÚMEROS ENTRE TRÊS ?')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
maior = max(n1, n2, n3)
menor = min(n1, n2, n3)
print(f'Entre os três números digitados: {n1}, {n2} e {n3}'
      f'\nO MAIOR é {maior}'
      f'\nO menor é {menor}')