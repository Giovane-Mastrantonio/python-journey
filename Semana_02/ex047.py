# Crie um programa que mostre na tela
# todos os números pares que estão no intervalo entre 1 e 50.
texto = 'NÚMEROS PARES DE 1 ATÉ 50'
print(f'{texto:=^50}')
for i in range(2,51,2): # desta forma utiliza menos o processador reduz quantidade de laços, repetições
    if i % 2 == 0:
        print(f'{i}, ', end='')

print('FIM')