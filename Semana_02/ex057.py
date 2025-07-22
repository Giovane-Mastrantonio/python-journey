# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
texto = 'LEITURA DO SEXO POR M OU F'
print(f'{texto:=^50}')
sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Digite o sexo [M/F]: ')).strip().upper()[0]

print(f'Voce Digitou certo. Sexo {sexo}')
