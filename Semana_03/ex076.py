# Crie um programa que tenha uma tupla única com nomes de produtos
# e seus respectivos preços, na sequência. No final, mostre uma listagem
# de preços, organizando os dados em forma tabular.
texto = 'NOMES DE PRDUTOS'
print(f'{texto:=^50}')

# Tupla com produtos e preços intercalados
produtos = (
    'Lápis', 1.75,
    'Borracha', 2.00,
    'Caderno', 15.90,
    'Estojo', 25.00,
    'Transferidor', 4.20,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canetas', 22.30,
    'Livro', 34.90
)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

# Percorre a tupla de 2 em 2: índice par = nome, índice ímpar = preço
for pos in range(0, len(produtos), 2):
    nome = produtos[pos]
    preco = produtos[pos + 1]
    # formatação: nome alinhado à esquerda, preço alinhado à direita com 2 casas decimais
    print(f'{nome:.<30}R${preco:>7.2f}')

print('-' * 40)


