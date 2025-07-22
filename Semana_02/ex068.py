# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

texto = 'JOGANDO PAR OU IMPAR'
print(f'{texto:=^50}')
vitorias = 0

while True:     # Entrada do jogador
    jogador = int(input("Digite um valor: "))
    escolha = ' '
    while escolha not in ('P', 'I'):
        escolha = input("Par ou Ímpar? [P/I]: ").strip().upper()

                # Computador escolhe número
    computador = randint(0, 10)
    total = jogador + computador

    print(f"Você jogou {jogador} e o computador {computador}. Total de {total}.", end=' ')
    print("DEU PAR" if total % 2 == 0 else "DEU ÍMPAR")

                # Verifica quem venceu
    if escolha == 'P':
        if total % 2 == 0:
            print("Você VENCEU!\n")
            vitorias += 1
        else:
            print("Você PERDEU!\n")
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print("Você VENCEU!\n")
            vitorias += 1
        else:
            print("Você PERDEU!\n")
            break
    print("Vamos jogar novamente...\n")
    print("=-" * 20)

print("=-" * 20)
print(f"GAME OVER! Você venceu {vitorias} vez(es) consecutivas.")
