# Crie um programa que leia quanto dinheiro ela tem na carteira e
# quantos dólares ela pode comprar
# Considere
# US$ 1,00 = R$ 5,49 => hoje 08/07/2025
# Euro = 6,45   Peso Argentino = 0,0043  Peso Uruguaio = 0,14
print('=== LÊ VALOR NA CARTEIRA E CONVERTE EM DÓLAR ===')
carteira = float(input('Digite o dinheiro da Carteira em reais, R$ '))
dolar = carteira / 5.49
p_argentino = carteira / 0.0043
P_uruguaio = carteira / 0.14
print('O dinheiro que tenho R$ {}, consigo comprar: '
      '\nUS$ {:.2f}'
      '\nARS$ {:.2f}'
      '\nUYU$ {:.2f}'.format(carteira, dolar, p_argentino, P_uruguaio))


