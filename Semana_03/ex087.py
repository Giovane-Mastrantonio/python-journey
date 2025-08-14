# Aprimore o desafio anterior (ex086), mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_coluna3 = 0
maior_linha2 = 0

# Preenchendo a matriz e processando ao mesmo tempo
for linha in range(3):
    for coluna in range(3):
        valor = int(input(f"Digite um valor para [{linha}, {coluna}]: "))
        matriz[linha][coluna] = valor

        if valor % 2 == 0:
            soma_pares += valor

        if coluna == 2:
            soma_coluna3 += valor

        if linha == 1:
            if coluna == 0 or valor > maior_linha2:
                maior_linha2 = valor

# Mostrando a matriz formatada
print("\nMatriz 3x3:")
for linha in matriz:
    for valor in linha:
        print(f"[{valor:^5}]", end=" ")
    print()

# Resultados
print(f"\nA) Soma dos valores pares: {soma_pares}")
print(f"B) Soma dos valores da terceira coluna: {soma_coluna3}")
print(f"C) Maior valor da segunda linha: {maior_linha2}")
