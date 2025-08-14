# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
texto = 'INFORMA O MAIOR DA LISTA'
print(f'{texto:=^50}\n')

def maior(*numeros):
    maior_valor = numeros[0]

    for numero in numeros:
        if numero > maior_valor:
            maior_valor = numero

    print(numeros)
    print( f"O maior valor informado foi: {maior_valor}" )
    print( "-" * 50 )
    return maior_valor


print( "Teste 1 - Números positivos:" )
maior( 2, 9, 4, 5, 7, 1 )
print()

print( "Teste 2 - Números com negativos:" )
maior( 4, 7, 0 )
print()

print( "Teste 3 - Números negativos:" )
maior( -10, -4, -22, -1 )
print()

print( "Teste 5 - Muitos números:" )
maior( 1, 3, 5, 7, 9, 2, 4, 6, 8, 10 )
print()

