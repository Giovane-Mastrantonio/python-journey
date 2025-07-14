# Crie um algoritmo que leia um número e
# mostre o seu dobro, triplo e raiz quadrada
print('=== MOSTRA DOBRO, TRIPLO E RAIZ QUADRADA DE UM NUMERO ===')
n1 = int(input('Digite um numero inteiro: '))
dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** (1/2)
print('O número digitado foi {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.2f}'.format(n1, dobro, triplo, raiz))
print('Sua raiz quadrada é {2:.2f}, Seu triplo {1}, seu Dobro {0}'.format(dobro, triplo, raiz))
