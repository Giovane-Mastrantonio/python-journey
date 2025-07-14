# Faça um programa que leia um número inteiro qualquer
# e mostre na tela a sua tabuada
# for é um laço de repetição
# o count é um contator que irá contar de 1 até o valor informado no parênteses
print('=== INFORME UM NÚMERO INTEIRO E FAREMOS SUA TABUADA COMPLETA ===')
n1 = int(input('Digite um número inteiro: '))

print('-' * 12)
for count in range(10):
    print("{} x {:2} = {}".format (n1, count+1, n1*(count+1)) )

print('-' * 12)
