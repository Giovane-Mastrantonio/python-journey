# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.
texto = 'SORTEANDO DADOS'
print(f'{texto:=^50}')
from random import randint
from time import sleep
from operator import itemgetter

# Criar o dicionário com os resultados dos jogadores
jogadores = {
    'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6),
}

# Mostrar os resultados dos dados
print("Resultados dos dados:")
for jogador, resultado in jogadores.items():
    print(f"{jogador} tirou {resultado} no dado.")
    sleep(1)

# Ordenar os jogadores pelo resultado do dado (maior para menor)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

# Mostrar o ranking
print("\n== Ranking dos jogadores ==")
for i, (jogador, resultado) in enumerate(ranking, start=1):
    print(f"{i}º lugar: {jogador} com {resultado}")
    sleep(0.5)
