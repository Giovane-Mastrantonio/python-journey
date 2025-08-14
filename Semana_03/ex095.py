# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização
# de detalhes do aproveitamento de cada jogador
# Se na opção de mostrar os dados for digitado um número de jogador inexistente,
# retornar "ERRO! Não existe jogador com o código tal! Tente novamente.
# E se for digitado 999 o programa encerra.
texto = 'TABELA DE JOGADORES - APRIMORADA'
print(f'{texto:=^50}')
jogadores = []

# Cadastro de jogadores
while True:
    jogador = {}
    gols = []

    jogador['nome'] = input( "Nome do jogador: " ).strip().title()
    partidas = int( input( f"Quantas partidas {jogador['nome']} jogou? " ) )

    for i in range( partidas ):
        gols.append( int( input( f"  Quantos gols na partida {i + 1}? " ) ) )

    jogador['gols'] = gols
    jogador['total'] = sum( gols )

    jogadores.append( jogador.copy() )

    while True:
        continuar = input( "Deseja adicionar outro jogador? [S/N]: " ).strip().upper()
        if continuar in 'SN':
            break
        print( "Erro! Digite apenas S ou N." )

    if continuar == 'N':
        break

# Mostrar resumo da tabela
print( "\n== TABELA DE JOGADORES ==" )
print( f"{'Cod':<5}{'Nome':<15}{'Gols':<20}{'Total':<6}" )
print( "-" * 50 )
for i, j in enumerate( jogadores ):
    print( f"{i:<5}{j['nome']:<15}{str( j['gols'] ):<20}{j['total']:<6}" )
print( "-" * 50 )

# Consulta de detalhes por código
while True:
    codigo = int( input( "Mostrar dados de qual jogador? (999 para sair): " ) )
    if codigo == 999:
        print( "Encerrando..." )
        break
    if codigo < 0 or codigo >= len( jogadores ):
        print( f"ERRO! Não existe jogador com o código {codigo}! Tente novamente." )
    else:
        print( f"== Detalhes do jogador {jogadores[codigo]['nome']}:" )
        for i, g in enumerate( jogadores[codigo]['gols'] ):
            print( f"  No jogo {i + 1} fez {g} gol(s)." )
