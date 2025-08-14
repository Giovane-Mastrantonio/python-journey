# Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre_os em uma lista única que mantenha separados os valores pares e
# ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

numeros = [[], []]  # Lista com duas sublistas: [pares, ímpares]

for i in range(7):
    valor = int(input(f"Digite o {i + 1}º valor: "))
    if valor % 2 == 0:
        numeros[0].append(valor)  # Pares
    else:
        numeros[1].append(valor)  # Ímpares

# Ordenando as sublistas
numeros[0].sort()
numeros[1].sort()

# Resultado
print(f"\nValores pares em ordem crescente: {numeros[0]}")
print(f"Valores ímpares em ordem crescente: {numeros[1]}")
