# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
# início, fim e passo e realize a contagem. Seu programa tem que realizar três contagens
# através da função criada:
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada
# Deve aceitar contagens de positivos para negativos se for regressiva e ao contrário também.
from time import sleep
texto = 'CONTADOR COM SALTOS'
print(f'{texto:=^50}')

def contador(inicio, fim, passo):

    print( f"Contagem de {inicio} até {fim}, de {abs( passo )} em {abs( passo )}:" )

    # Se o passo for 0, define como 1 para evitar loop infinito
    if passo == 0:
        passo = 1

    # Ajusta o passo automaticamente baseado na direção da contagem
    if inicio > fim and passo > 0:
        passo = -passo
    elif inicio < fim and passo < 0:
        passo = -passo

    # Realiza a contagem
    atual = inicio
    numeros = []

    if passo > 0:  # Contagem crescente
        while atual <= fim:
            numeros.append( str( atual ) )
            atual += passo
    else:  # Contagem decrescente
        while atual >= fim:
            numeros.append( str( atual ) )
            atual += passo

    # Exibe a contagem
    print( " → ".join( numeros ) )
    print( "FIM!" )
    print( "-" * 40 )


# A) De 1 até 10, de 1 em 1
print( "A) Contagem de 1 até 10, de 1 em 1" )
contador( 1, 10, 1 )
print()

# B) De 10 até 0, de 2 em 2
print( "B) Contagem de 10 até 0, de 2 em 2" )
contador( 10, 0, 2 )
print()

# C) Contagem personalizada
print( "C) Contagem personalizada" )
print( "Agora é sua vez de personalizar!" )

inicio = int( input( "Início: " ) )
fim = int( input( "Fim: " ) )
passo = int( input( "Passo: " ) )

print()
contador( inicio, fim, passo )
print()
