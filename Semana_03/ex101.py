# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
# o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa
# tem voto negado, opcional ou obrigatório nas eleições.
from datetime import datetime

def voto(ano_nascimento):
    """Determina a situação de voto baseada no ano de nascimento.

    Args:
        ano_nascimento (int): Ano de nascimento da pessoa

    Returns:
        str: Status do voto ("VOTO NEGADO", "VOTO OPCIONAL" ou "VOTO OBRIGATÓRIO")
    """
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento

    if idade < 16:
        return "VOTO NEGADO"
    elif idade < 18 or idade >= 70:
        return "VOTO OPCIONAL"
    else:
        return "VOTO OBRIGATÓRIO"


def calcular_idade(ano_nascimento):
    """Calcula a idade baseada no ano de nascimento."""
    return datetime.now().year - ano_nascimento


def main():
    """Função principal do programa."""
    ano_nascimento = int( input( "Digite o ano de nascimento: " ) )

    resultado = voto( ano_nascimento )
    idade = calcular_idade( ano_nascimento )

    print( f"Idade: {idade} anos" )
    print( f"Situação: {resultado}" )


if __name__ == "__main__":
    main()