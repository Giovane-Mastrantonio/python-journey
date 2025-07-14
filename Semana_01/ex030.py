# Crie um programa que leia um número inteiro
# e mostre na tela se ele é PAR ou IMPAR
print('===== PROGRAMA PAR OU IMPAR =====')
n = int(input('Digite um número inteiro '))
# if n % 2 == 0:
#     print('PAR')
# else:
#     print('IMPAR')

print('IMPAR' if n % 2 != 0 else 'PAR')