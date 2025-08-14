# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro
# que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(numero, show=False):
    """Calcula o fatorial de um número.

    Args:
        numero (int): Número para calcular o fatorial
        show (bool): Se True, mostra o processo de cálculo

    Returns:
        int: O valor do fatorial
    """
    if numero < 0:
        return None

    if numero == 0 or numero == 1:
        if show:
            print( f"{numero}! = 1" )
        return 1

    resultado = 1
    processo = []

    for i in range( numero, 0, -1 ):
        processo.append( str( i ) )
        resultado *= i

    if show:
        calculo = " × ".join( processo )
        print( f"{numero}! = {calculo} = {resultado}" )

    return resultado


def main():
    """Função principal do programa."""
    numero = int( input( "Digite um número para calcular o fatorial: " ) )
    mostrar = input( "Mostrar o processo de cálculo? (s/n): " ).lower() == 's'

    resultado = fatorial( numero, mostrar )

    if resultado is None:
        print( "Erro: Não é possível calcular fatorial de número negativo!" )
    else:
        if not mostrar:
            print( f"{numero}! = {resultado}" )


if __name__ == "__main__":
    main()