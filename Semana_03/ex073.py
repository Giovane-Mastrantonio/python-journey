# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato
# Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# A)Apenas os primeiros 5 colocados.
# B)Os últimos 4 colocados
# C)Uma lista com os times em ordem alfabética
# D)Em que posição na tabela está o time da Chapecoense'''

texto = '20 PRIMEIROS TIMES DO BRASILEIRÃO'
print(f'{texto:=^50}')

tabela = (
    'Palmeiras', 'Botafogo', 'Grêmio', 'Flamengo', 'Atlético-MG',
    'Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza',
    'São Paulo', 'Cuiabá', 'Cruzeiro', 'Chapecoense', 'Vasco da Gama',
    'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG'
)
print('--' * 30)
# A) Os 5 primeiros colocados
print('A) Os 5 primeiros colocados são:')
print(tabela[:5])

print('--' * 30)
# B) Os 4 últimos colocados
print('B) Os 4 últimos colocados são:')
print(tabela[-4:])

print('--' * 30)
# C) Times em ordem alfabética
print('C) Times em ordem alfabética:')
print(sorted(tabela))

print('--' * 30)
# D) Posição da Chapecoense
print('D) Posição da Chapecoense:')
if 'Chapecoense' in tabela:
    posicao = tabela.index('Chapecoense') + 1
    print(f'A Chapecoense está na {posicao}ª posição.')
else:
    print('Chapecoense não está entre os 20 primeiros colocados.')
print('--' * 30)
