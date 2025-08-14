# Modifique as funções que foram criadas no desafio 107 para que elas aceitem
# um parâmetro a mais, informando se o valor retornado por elas vai ser ou não
# formatado pela função moeda(), desenvolvida no desafio 108.

# programa_teste.py - Programa para testar o módulo moeda

from ex107 import moeda

# Valor inicial para os testes
valor_original = float(input('Digite um valor: '))

print("=" * 50)
print("TESTANDO O MÓDULO MOEDA")
print("=" * 50)

print(f"Valor original: R$ {valor_original:.2f}")
print()

# Testando a função aumentar()
aumento = 15  # 15%
valor_aumentado = moeda.aumentar(valor_original, aumento)
print(f"Aumentar {aumento}%: R$ {valor_aumentado:.2f}")

# Testando a função diminuir()
desconto = 10  # 10%
valor_diminuido = moeda.diminuir(valor_original, desconto)
print(f"Diminuir {desconto}%: R$ {valor_diminuido:.2f}")

# Testando a função dobro()
valor_dobrado = moeda.dobro(valor_original)
print(f"Dobro do valor: R$ {valor_dobrado:.2f}")

# Testando a função metade()
valor_metade = moeda.metade(valor_original)
print(f"Metade do valor: R$ {valor_metade:.2f}")

print()
print("=" * 50)
print("EXEMPLO PRÁTICO")
print("=" * 50)

# Exemplo prático com um produto
preco_produto = 250.00
print(f"Preço do produto: R$ {preco_produto:.2f}")

# Aplicando desconto de 20%
preco_desconto = moeda.diminuir(preco_produto, 20)
print(f"Com desconto de 20%: R$ {preco_desconto:.2f}")

# Aplicando aumento de 5% (impostos)
preco_final = moeda.aumentar(preco_desconto, 5)
print(f"Com impostos de 5%: R$ {preco_final:.2f}")

# Calculando parcelamento em 2x
parcela = moeda.metade(preco_final)
print(f"Parcelado em 2x: R$ {parcela:.2f} cada parcela")