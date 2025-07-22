# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu valor normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto;
# em até 2x no cartão: valor normal;
# 3x ou mais no cartão: 20% de juros
texto = 'CALCULADORA DE CONDIÇÕES DE PAGAMENTO'
print(f'{texto:=^60}')
valor = float(input('Qual o valor das compras: R$ '))
condicao = int(input('Formas de pagamento?'
                     '\n[ 1 ] A VISTA dinheiro/cheque'
                     '\n[ 2 ] A VISTA cartão'
                     '\n[ 3 ] Em até 2x no cartão'
                     '\n[ 4 ] Em 3x ou mais no cartão'
                     '\n Informe a opção ==> '))
if condicao == 1:
    total = valor - (valor * 0.10)
    print(f'Você irá pagar R$ {total:.2f}, já com desconto de 10%.')
elif condicao == 2:
    total = valor - (valor * 0.05)
    print(f'Você irá pagar R$ {total:.2f}, já com desconto de 5%.')
elif condicao == 3:
    total = valor / 2
    print(f'Você irá pagar em 2x de R$ {total:.2f} sem juros.')
elif condicao == 4:
    parcelas = int(input('Quantas parcelas irá pagar? '))
    total = valor + (valor * 0.20)
    pacelasTotal = total / parcelas
    print(f'Sua compra será parcelada em {parcelas}x de R$ {pacelasTotal:.2f} com juros.'
          f'\nSua compra irá custar um valor de R$ {total:.2f}')
else:
    print('Você não digitou uma opção válida')
