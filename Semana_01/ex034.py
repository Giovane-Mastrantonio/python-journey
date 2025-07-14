# Escreva um programa que pergunte o salário de um funcionário e calcule
# o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%
print('CALCULANDO AUMENTO DE SALÁRIOS')
salario = float(input('Informe seu salario: '))
if salario > 1250:
    salario = salario + (salario * 10 / 100)
    print(f'Seu novo salário com 10% será de R$ {salario:.2f}')
else:
    salario = salario + (salario * 15 / 100)
    print(f'Seu novo salário será de R$ {salario:.2f}')