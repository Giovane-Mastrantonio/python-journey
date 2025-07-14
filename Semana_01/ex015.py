# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e $0,15 por KM rodado

print('=== DIGITE QUANTOS DIAS FICOU COM O CARRO E QUANTOS KM RODADOS ===')
dias = int(input('Quantos dias você ficou com o carro: '))
km = float(input('Quantos KM você rodou: '))
pagar = (dias * 60) + (km * 0.15)
print('O total a pagar é de R$ {:.2f}'.format(pagar))
