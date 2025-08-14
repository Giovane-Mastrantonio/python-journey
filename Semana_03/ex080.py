# Crie um programa onde o usuário possa digitar cinco valores numéricos e
# cadastre-os em uma lista, já na posição correta de inserção (sem usar
# o sort()). No final, mostre a lista ordenada na tela.
texto = 'CINCO NÚMEROS ORDENADOS SEM SORT()'
print(f'{texto:=^50}')
lista_valores = []
for c in range(0, 5):
    valores = int(input(f'Digite o {c+1}º valor inteiro: '))
    if not lista_valores or valores > lista_valores[-1]:
        lista_valores.append( valores )
    else:
        pos = 0
        # Encontra a posição correta para inserção
        while pos < len( lista_valores ):
            if valores <= lista_valores[pos]:
                lista_valores.insert( pos, valores )
                break
            pos += 1

print( '\nLista ordenada:', lista_valores )