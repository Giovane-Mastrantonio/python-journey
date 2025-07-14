# Faça um algoritmo que leia o salário de um funcionário e
# mostre seu novo salário, com 15% de aumento
print('=== LÊ SALÁRIO E APLICA 15% DE AUMENTO ===')
salario = float(input('Digite seu salario em reais: R$ '))
aumento = salario + (salario * 0.15)
print('O salario de R$ {:.2f} foi aumentado em 15%, ficando R$ {:.2f}'.format(salario, aumento))