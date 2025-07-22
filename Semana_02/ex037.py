# Escreva um programa que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal. (bases numéricas)
print('==========CONVERSOR DE INTEIRO==============')
numero = int(input('Digite um número inteiro: '))
print("Escolha uma base para conversão:")
print("[ 1 ] Converter para BINÁRIO")
print("[ 2 ] Converter para OCTAL")
print("[ 3 ] Converter para HEXADECIMAL")
escolhido = int(input('Infome sua escolha: '))

if escolhido == 1:
    print(f'{numero} convertido para BINÁRIO é = {bin(numero)[2:]}') #o [2:] corta os dois primeiros números
elif escolhido == 2:
    print(f'{numero} convertido para OCTAL é = {oct(numero)[2:]}')
elif escolhido == 3:
    print(f'{numero} convertido para HEXADECIMAL é = {hex(numero)[2:]}')
else:
    print('Opção invalida!')


