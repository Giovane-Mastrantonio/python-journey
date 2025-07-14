# Faça um programa que leia um número de 0 a 9999 e mostre na
# tela cada um dos digitos separados
# EX: digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1
print('=== DIGITE UM NÚMERO DE 0 A 9999 ===')
numero = (input('Digite um número de 0 a 9999: ')).zfill(4) # Preenche com zeros à esquerda se necessário
print(f'''Do número digitado temos:
Sua unidade é o {numero[3]}
Sua dezena é o {numero[2]}
Sua centena é o {numero[1]}
E seu milhar é o {numero[0]}''')

# OUTRA FORMA DE SER FEITO APENAS COM MATEMÁTICA
unidade = int(numero) // 1 % 10
dezena = int(numero) // 10 % 10
centena = int(numero) // 100 % 10
milhar = int(numero) // 1000 % 10
print(f'\n'
      f'Unidade: {unidade}, Dezena: {dezena}, Centena: {centena}, Milhar: {milhar}')