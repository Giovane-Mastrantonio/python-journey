# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de
# gols feitos durante o campeonato.

texto = 'TABELA DE JOGADOR'
print(f'{texto:=^50}')
jogador = {}

# Ler o nome e número de partidas
jogador['nome'] = input("Nome do jogador: ")
num_partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

# Lista para armazenar os gols por partida
gols = []

# Ler os gols em cada partida
for i in range(num_partidas):
    gols.append(int(input(f"  Quantos gols na partida {i + 1}? ")))

# Adicionar os dados ao dicionário
jogador['gols'] = gols
jogador['total'] = sum(gols)

# Exibir o resultado
print("\n== APROVEITAMENTO DO JOGADOR ==")
print(jogador)

# Exibição detalhada
print(f"\nO jogador {jogador['nome']} jogou {num_partidas} partidas.")
for i, g in enumerate(jogador['gols']):
    print(f"  → Na partida {i + 1} fez {g} gol(s).")
print(f"Foi um total de {jogador['total']} gol(s).")
