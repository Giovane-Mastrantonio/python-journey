# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
texto = 'LISTA DE NÚMEROS - TRATAMENTO'
print(f'{texto:=^50}')
        # criando a lista através de entradas do usuário
lista_numeros = []
for c in range(0, 5):
    numeros = int(input(f'Digite um valor inteiro para a posição {c}: '))
    lista_numeros.append(numeros)

        # encontrando o maior e menor valor
maior = max(lista_numeros)
menor = min(lista_numeros)

        # encontrar a posição do maior e menor na lista
posicao_maior = [i for i, numeros in enumerate(lista_numeros) if numeros == maior]
posicao_menor = [i for i, numeros in enumerate(lista_numeros) if numeros == menor]
print('▬' * 20)
# Encontrar as posições do maior valor
# posicoes_maior = []
# for i, valor in enumerate(valores):
#     if valor == maior:
#         posicoes_maior.append(i)
#
# # Encontrar as posições do menor valor
# posicoes_menor = []
# for i, valor in enumerate(valores):
#     if valor == menor:
#         posicoes_menor.append(i)
print(lista_numeros)
print('▬' * 20)

print(f'Maior valor: {maior}')
print(f'A posição do maior está no índice: {posicao_maior}')
print(f'Menor valor: {menor}')
print(f'A posição do menor está no índice: {posicao_menor}')

print('▬' * 20)
lista_numeros.sort()
print(f'Aqui a lista em ordem crescente\n {lista_numeros}')
print('▬' * 20)

