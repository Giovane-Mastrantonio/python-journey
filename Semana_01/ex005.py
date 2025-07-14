#Faça um programa que leia um número inteiro
# e mostre na tela o seu sucessor e seu antecessor
# Para ativar o negrito, você usa \033[1m antes do texto e \033[0m para desativá-lo.

print('=== MOSTRA SUCESSOR E ANTECESSOR DE UM NUMERO INTEIRO ===')
n1 = int(input('Digite um numero inteiro: '))
antecessor = n1 - 1
sucessor = n1 + 1
print('O numero \033[1mdigitado\033[1m foi {} seu \033[1mantecessor\033[0m é {} e seu \033[1msucessor\033[0m é {}'.format(n1, antecessor, sucessor))
