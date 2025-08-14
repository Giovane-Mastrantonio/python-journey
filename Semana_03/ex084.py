# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma lista com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = []
maior_peso = menor_peso = 0

while True:
    nome = input("Nome da pessoa: ")
    peso = float(input("Peso da pessoa (kg): "))

    pessoas.append([nome, peso])

    if len(pessoas) == 1:
        maior_peso = menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

    continuar = input("Deseja cadastrar outra pessoa? [S/N] ").strip().upper()
    if continuar == 'N':
        break

# Resultados finais
print(f"\nA) Total de pessoas cadastradas: {len(pessoas)}")

print(f"B) Pessoas com maior peso ({maior_peso}kg): ", end="")
print(', '.join([p[0] for p in pessoas if p[1] == maior_peso]))

print(f"C) Pessoas com menor peso ({menor_peso}kg): ", end="")
print(', '.join([p[0] for p in pessoas if p[1] == menor_peso]))
