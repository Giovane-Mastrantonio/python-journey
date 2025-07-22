# Refaça o DESAFIO 9,
# mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.
texto = 'INFORME UM NÚMERO INTEIRO E FAREMOS SUA TABUADA COMPLETA'
print(f'{texto:=^50}')
n1 = int(input('Digite um número inteiro: '))
print('-' * 12)
for count in range(1, 11):
    print(f'{n1} x {count:2} = {n1*count}')
print('-' * 12)
