# Faça um programa que calcule a soma entre todos os números ímpares
# que são múltiplos de três e que se encontram no intervalo de 1 até 500
texto = 'CALCULADOR ESPECÍFICO'
print(f'{texto:=^50}')
print('Esse é o resultado da soma entre todos os números ímpares'
      ' que são múltiplos de três e que se encontram no intervalo de 1 até 500')
total = 0
cont = 0
for i in range(1,501,2):
    if i % 3 == 0 and i % 2 != 0:
        total += i
        cont += 1

print(f'A soma dos {cont} números é igual a {total}')

