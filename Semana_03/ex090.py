# Faça um programa que leia nome e média de um aluno, guardando também a
# situaçao em um dicionário. No final mostre o conteúdo da estrutura na tela
# MODELO:
# ENTRADA => Nome: Fulano / Média de Fulano:
# SAÍDA => Nome é igual a Fulano / Média é igual a xx.x / Situação é igual a Aprovado
# Criar o dicionário para armazenar as informações do aluno
texto = 'PROGRAMA DE MÉDIAS DE ALUNOS'
print(f'{texto:=^50}')
# inicializa o dicionário
aluno = {}

# Ler os dados do usuário
aluno['nome'] = input("Nome do aluno: ")
aluno['media'] = float(input(f"Média de {aluno['nome']}: "))

# Verificar a situação do aluno
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

# Exibir o resultado
print("\n== Resultado ==")
for chave, valor in aluno.items():
    print(f"{chave.capitalize()}: {valor}")
