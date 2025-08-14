# Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
texto = 'CRIANDO LISTAS SEM REPETIÇÃO DE ELEMENTOS'
print(f'{texto:=^50}')

numeros = []

while True:
    entrada = input( "Digite um número (ou 'sair' para encerrar): " ).strip()
    if entrada.lower() == 'sair':
        if not numeros:  # Se a lista estiver vazia
            print( "Você saiu sem digitar nenhum valor." )
        break  # Sai do loop
    if entrada.isdigit():  # Verifica se é um número inteiro positivo
        num = int( entrada )
        if num not in numeros:
            numeros.append( num )
        else:
            print( f"O número {num} já está na lista e será ignorado." )
    else:
        print( "Por favor, digite apenas números inteiros positivos!" )

# Mostra os números únicos em ordem crescente (se houver valores)
if numeros:
    print( "\nValores únicos digitados (em ordem crescente):" )
    print( sorted( numeros ) )