# Faça um programa que tenha uma função chamada área(), que receba as dimensões
# de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(largura, comprimento):
    return largura * comprimento


def main():
    print( "=== CALCULADORA DE ÁREA DE TERRENO ===" )
    print()

    # Solicita as dimensões do terreno
    largura = float( input( "Digite a largura do terreno (em metros): " ) )
    comprimento = float( input( "Digite o comprimento do terreno (em metros): " ) )

    # Verifica se os valores são positivos
    if largura <= 0 or comprimento <= 0:
        print( "Erro: As dimensões devem ser valores positivos!" )
        return

    # Calcula a área usando a função
    resultado = area( largura, comprimento )

    # Mostra o resultado
    print( f"\nResultado:" )
    print( f"Largura: {largura} m" )
    print( f"Comprimento: {comprimento} m" )
    print( f"Área do terreno: {resultado} m²" )


# Exemplos de uso da função
if __name__ == "__main__":
    # Executa o programa principal
    main()
