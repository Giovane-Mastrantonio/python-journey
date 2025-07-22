# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos
texto = 'CLASSIFICANDO PESSOAS'
print(f'{texto:=^50}')
somaIdades = 0
nomHomemMaisVelho = ""
idadeHomemMaisVelho = 0
mulheresMenosDe20 = 0

for i in range(1, 5):
    print(f"---- {i}ª PESSOA ----")
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()

    somaIdades += idade

    if sexo == "M":
        if idade > idadeHomemMaisVelho:  # verifica se é o mais velho
            idadeHomemMaisVelho = idade
            nomHomemMaisVelho = nome

    if sexo == "F" and idade < 20:
        mulheresMenosDe20 += 1

# cálculos finais
media_idade = somaIdades / 4

# saída
print("\n===== RESULTADO =====")
print(f"A média de idade do grupo é {media_idade:.1f} anos.")
if nomHomemMaisVelho:
    print(f"O homem mais velho é {nomHomemMaisVelho} com {idadeHomemMaisVelho} anos.")
else:
    print("Não há homens no grupo.")
print(f"Neste grupo tem {mulheresMenosDe20} mulheres com menos de 20 anos.")
