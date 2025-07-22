# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Caulcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
print('========CALCULADORA DE EMPRÉSTIMO BANCÁRIO============')
valorCasa = float(input('Qual o valor da casa: R$ '))
salarioComprador = float(input('Qual o salario do comprador: R$ '))
anosPagamento = int(input('Em quantos anos vai pagar? '))
prestacaoMensal = (valorCasa / anosPagamento) / 12

if prestacaoMensal > (salarioComprador * (30/100)):
    print(f'Empréstimo NEGADO!'
          f'\nA prestação de RS {prestacaoMensal:.2f} excede 30% do seu salário de RS {salarioComprador:.2f}.')
else:
    print(f'Empréstimo APROVADO!'
          f'\nParcelas mensais no valor de R$ {prestacaoMensal:.2f} ')