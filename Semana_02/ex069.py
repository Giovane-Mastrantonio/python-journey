# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
texto = 'CADASTRO DE PESSOAS'
print(f'{texto:=^50}\n')
mais18 = 0
homens = 0
mulheres_menor20 = 0
conta_cadastros = 0

while True:
    print("CADASTRE UMA PESSOA")
    print("-" * 30)
    conta_cadastros += 1
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in ('M', 'F'):
        sexo = input("Sexo: [M/F] ").strip().upper()

    # Contagens
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menor20 += 1

    # Deseja continuar?
    continuar = ' '
    while continuar not in ('S', 'N'):
        continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar == 'N':
        break
    print("-" * 30)

# Resultados finais
print("\n========== RESULTADOS ==========")
print(f"A) Pessoas com mais de 18 anos: {mais18}")
print(f"B) Homens cadastrados: {homens}")
print(f"C) Mulheres com menos de 20 anos: {mulheres_menor20}")
print(f"D) Total de cadastros: {conta_cadastros}")
print("================================")
