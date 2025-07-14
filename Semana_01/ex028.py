# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
# pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu
import random

print('===== DESCUBRA QUAL NÚMERO O COMPUTADOR PENSOU DE 0 A 5 =====')
n = random.randint(0, 5)
nusuario = int(input('Digite seu número da sorte de 0 a 5: '))

if n == nusuario:
    print('Você VENCEU!!')
else:
    print(f'Você PERDEU! O número sorteado foi {n}.')
