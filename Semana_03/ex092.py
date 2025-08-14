# Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-os (com idade) em um dicionário se por acaso a CTPS for
# diferente de zero, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime

texto = 'PROGRAMA APOSENTADORIA'
print(f'{texto:=^50}')

# Obter o ano atual
ano_atual = datetime.now().year

# Criar o dicionário para armazenar os dados da pessoa
pessoa = {}

# Ler os dados básicos
pessoa['nome'] = input("Nome: ")
ano_nasc = int(input("Ano de nascimento: "))
pessoa['idade'] = ano_atual - ano_nasc
pessoa['ctps'] = int(input("Número da carteira de trabalho (0 se não tem): "))

# Se tiver CTPS (diferente de 0), pede mais dados
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input("Ano de contratação: "))
    pessoa['salario'] = float(input("Salário: R$ "))
    anos_contribuicao = 35
    pessoa['aposentadoria'] = pessoa['idade'] + (pessoa['contratacao'] + anos_contribuicao - ano_atual)

# Exibir os dados cadastrados
print("\n== DADOS CADASTRADOS ==")
for chave, valor in pessoa.items():
    print(f"{chave.capitalize()}: {valor}")
