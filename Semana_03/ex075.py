# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
# em uma tupla. No final, mostre:
# A) QUANTAS VEZES APARECEU O VALOR 9.
# B) EM QUE POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR 3.
# C) QUAIS FORAM OS NÚMEROS PARES.
# se digitar um número errado tem que impedir
texto = 'LENDO NÚMEROS E QUALIFICANDO'
print(f'{texto:=^50}')
# Lendo 4 valores e guardando em uma tupla
valores = (
    int(input('Digite o 1º valor: ')),
    int(input('Digite o 2º valor: ')),
    int(input('Digite o 3º valor: ')),
    int(input('Digite o 4º valor: '))
)

print('--' * 30)
print(f'Você digitou os valores: {valores}')

# A) Quantas vezes apareceu o valor 9
print(f'O valor 9 apareceu {valores.count(9)} vezes.')

# B) Em que posição foi digitado o primeiro valor 3
if 3 in valores:
    print(f'O valor 3 apareceu primeiro na posição {valores.index(3)+1}ª.')
else:
    print('O valor 3 não foi digitado nenhuma vez.')

# C) Quais foram os números pares
pares = [n for n in valores if n % 2 == 0]

        # Se a lista não estiver vazia
if pares:
    print('Os números pares digitados foram:', end=' ')
    for p in pares:
        print(p, end=' ')
    print()
else:
    print('Nenhum número par foi digitado.')

