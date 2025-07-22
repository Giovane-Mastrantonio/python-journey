# Crie um programa que leia uma frase qualquer e
# diga se ela é um palíndromo, desconsiderando os espaços.
# EXEMPLOS de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA,
# O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA
texto = 'TESTANDO FRASES SE SÃO PALÍNDROMOS'
print(f'{texto:=^50}')
frase = str(input('Digite uma frase: ')).upper().replace(' ', '')
fraseInvertida = frase[::-1].upper().replace(' ', '')
if frase == fraseInvertida:
    print('É um PALÍNDROMO!')
else:
    print('NÃO é um PALÍNDROMO!')
