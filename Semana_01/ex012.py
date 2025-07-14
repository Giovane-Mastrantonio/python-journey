# Faça um algoritmo que leia o preço de um produto e
# mostre seu novo preço, com 5% de desconto
print('=== LÊ UM PRODUTO E DEPOIS APLICA 5% DE DESCONTO ===')
produto = float(input('Digite sua Produto: '))
desconto = produto * (5 / 100)
valorfinal = produto - (desconto)
print('O preço do produto é R$ {}, mas com 5% de desconto fica R$ {:.2f}'.format(produto, valorfinal))
print('=== Desconto de {:.2f} ==='.format(desconto))