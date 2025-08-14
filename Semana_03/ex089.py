# Crie um programa que leia nome e duas notas de vários alunos e guarde
# tudo em uma lista composta. No final, mostre um boletim contendo a média
# de cada um e permita que o usuário possa mostrar as notas de cada aluno
# individualmente.

alunos = []

# Cadastro de alunos
while True:
    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2

    alunos.append([nome, [nota1, nota2], media])

    continuar = input("Deseja continuar? [S/N] ").strip().upper()
    if continuar == 'N':
        break

# Exibindo o boletim
print("\n{:<4} {:<10} {:>8}".format("No.", "NOME", "MÉDIA"))
print("-" * 26)
for i, aluno in enumerate(alunos):
    print("{:<4} {:<10} {:>8.1f}".format(i, aluno[0], aluno[2]))

# Consulta de notas individuais
while True:
    opcao = int(input("\nMostrar notas de qual aluno?\n"
                      "Digite o número do aluno (999 para sair): "))
    if opcao == 999:
        print("Encerrando...")
        break
    if 0 <= opcao < len(alunos):
        nome = alunos[opcao][0]
        notas = alunos[opcao][1]
        print(f"Notas de {nome}: {notas[0]} e {notas[1]}")
    else:
        print("Número inválido. Tente novamente.")
