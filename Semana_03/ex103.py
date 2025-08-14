# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros
# opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser
# capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado
# corretamente.

def ficha(nome="<desconhecido>", gols=0):
    """Exibe a ficha de um jogador.

    Args:
        nome (str): Nome do jogador (opcional)
        gols (int): Quantidade de gols marcados (opcional)
    """
    nome_final = nome if nome.strip() else "<desconhecido>"
    gols_final = gols if isinstance( gols, int ) and gols >= 0 else 0

    print( f"O jogador {nome_final} fez {gols_final} gol(s) no campeonato." )


def obter_nome():
    """Obtém o nome do jogador."""
    return input( "Nome do jogador: " )


def obter_gols():
    """Obtém a quantidade de gols."""
    entrada = input( "Número de gols: " )
    if entrada.isdigit():
        return int( entrada )
    return 0


def main():
    """Função principal do programa."""
    print( "FICHA DO JOGADOR" )
    print( "-" * 20 )

    nome = obter_nome()
    gols = obter_gols()

    ficha( nome, gols )


if __name__ == "__main__":
    main()