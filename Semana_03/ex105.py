# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação
# Adicione também as docstrings da função.

def notas(*args):
    """Analisa notas de alunos e retorna estatísticas.

    Args:
        *args: Notas dos alunos (números)

    Returns:
        dict: Dicionário com análise das notas contendo:
            - total: Quantidade de notas
            - maior: Maior nota
            - menor: Menor nota
            - media: Média da turma
            - situacao: Situação baseada na média
    """
    if not args:
        return {
            'total': 0,
            'maior': 0,
            'menor': 0,
            'media': 0,
            'situacao': 'Nenhuma nota informada'
        }

    total = len( args )
    maior = max( args )
    menor = min( args )
    media = sum( args ) / total

    if media >= 7:
        situacao = 'BOA'
    elif media >= 5:
        situacao = 'RAZOÁVEL'
    else:
        situacao = 'RUIM'

    return {
        'total': total,
        'maior': maior,
        'menor': menor,
        'media': media,
        'situacao': situacao
    }


def exibir_resultado(resultado):
    """Exibe o resultado da análise de forma formatada."""
    print( f"Total de notas: {resultado['total']}" )
    print( f"Maior nota: {resultado['maior']}" )
    print( f"Menor nota: {resultado['menor']}" )
    print( f"Média da turma: {resultado['media']:.1f}" )
    print( f"Situação: {resultado['situacao']}" )


def main():
    """Função principal do programa."""
    print( "ANÁLISE DE NOTAS DA TURMA" )
    print( "-" * 30 )

    # Exemplos de uso
    print( "Exemplo 1:" )
    resultado1 = notas( 5.5, 9.5, 10, 6.5 )
    exibir_resultado( resultado1 )

    print( "\nExemplo 2:" )
    resultado2 = notas( 7, 8, 9, 8.5, 7.5 )
    exibir_resultado( resultado2 )

    print( "\nExemplo 3:" )
    resultado3 = notas( 3, 4, 2.5 )
    exibir_resultado( resultado3 )

    print( "\nExemplo 4:" )
    resultado4 = notas()
    exibir_resultado( resultado4 )


if __name__ == "__main__":
    main()

# help(notas)