# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato
texto = 'SIMULADOR DE COMPRAS'
print(f'{texto:=^50}')
total_gasto = 0
mais_1000 = 0
produto_mais_barato = ''
preco_mais_barato = None  # ainda não definido

while True:
    print("-" * 30)
    nome = input("Nome do produto: ").strip()
    preco = float(input("Preço do produto: R$ "))

    # Soma ao total
    total_gasto += preco

    # Conta produtos acima de 1000
    if preco > 1000:
        mais_1000 += 1

    # Verifica produto mais barato
    if preco_mais_barato is None or preco < preco_mais_barato:
        preco_mais_barato = preco
        produto_mais_barato = nome

    # Continuar ou não?
    continuar = ' '
    while continuar not in ('S', 'N'):
        continuar = input("Quer continuar? [S/N]: ").strip().upper()
    if continuar == 'N':
        break

# Mostra os resultados
print("\n========== RESULTADOS ==========")
print(f"A) Total gasto na compra: R$ {total_gasto:.2f}")
print(f"B) Produtos que custam mais de R$1000: {mais_1000}")
print(f"C) Produto mais barato: {produto_mais_barato} (R$ {preco_mais_barato:.2f})")
print("================================")
