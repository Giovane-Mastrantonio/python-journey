# Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
texto = 'SOMA ENTRE PARES'
print(f'{texto:=^40}')
acumulador = 0
cont = 0
for c in range(1, 7):
        numeros = int(input(f'Digite o {c}º número inteiro: '))
        if numeros % 2 == 0:
            acumulador += numeros
            cont+=1
print(f'A soma dos {cont} números pares  é {acumulador}')
print('-' * 12)