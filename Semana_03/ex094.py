# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas
# B) A média de idade do grupo.  C) Uma lista com todas as mulheres.  D) Uma lista com todas as pessoas com
# idade acima da média
texto = 'LISTA DE PESSOAS'
print(f'{texto:=^50}')
grupo = []
soma_idades = 0

while True:
    pessoa = {}
    pessoa['nome'] = input( "Nome: " ).strip().title()

    # Garantir que o sexo seja 'M' ou 'F'
    while True:
        sexo = input( "Sexo [M/F]: " ).strip().upper()
        if sexo in 'MF':
            pessoa['sexo'] = sexo
            break
        print( "Erro! Digite apenas M ou F." )

    pessoa['idade'] = int( input( "Idade: " ) )
    soma_idades += pessoa['idade']

    grupo.append( pessoa.copy() )

    # Garantir que a resposta seja 'S' ou 'N'
    while True:
        continuar = input( "Deseja continuar? [S/N]: " ).strip().upper()
        if continuar in 'SN':
            break
        print( "Erro! Digite apenas S ou N." )

    if continuar == 'N':
        break

# Cálculo da média
media_idade = soma_idades / len( grupo )

# Exibir resultados
print( "\n== RESULTADOS ==" )
print( f"A) Total de pessoas cadastradas: {len( grupo )}" )
print( f"B) Média de idade: {media_idade:.2f} anos" )

# Lista com todas as mulheres
mulheres = [p['nome'] for p in grupo if p['sexo'] == 'F']
print( f"C) Mulheres cadastradas: {', '.join( mulheres ) if mulheres else 'Nenhuma'}" )

# Lista com pessoas acima da média
acima_da_media = [p for p in grupo if p['idade'] > media_idade]
print( "D) Pessoas com idade acima da média:" )
for p in acima_da_media:
    print( f"    Nome: {p['nome']}, Sexo: {p['sexo']}, Idade: {p['idade']}" )
