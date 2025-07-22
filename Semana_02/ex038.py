# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais
print('======COMPARA DOIS NÚMEROS======')
primeiroNumero = int(input('Digite o primeiro número: '))
segundoNumero = int(input('Digite o segundo número: '))
if primeiroNumero > segundoNumero:
    print(f'O Primeiro número digitado, {primeiroNumero} é MAIOR do que o segundo, {segundoNumero}')
elif primeiroNumero < segundoNumero:
    print(f'O Segundo número digitado, {segundoNumero} é MAIOR do que o primeiro, {primeiroNumero}')
else:
    print('Não existe valor maior, os dois são iguais')