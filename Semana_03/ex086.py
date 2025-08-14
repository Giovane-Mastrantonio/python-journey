# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com
# valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formação correta

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Preenchendo a matriz
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f"Digite um valor para [{linha}, {coluna}]: "))

# Mostrando a matriz formatada
print("\nMatriz 3x3:")
for linha in matriz:
    for valor in linha:
        print(f"[{valor:^5}]", end=" ")
    print()
