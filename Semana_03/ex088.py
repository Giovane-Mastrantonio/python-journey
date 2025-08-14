# Faça um programa que ajude um jogador da MEGA SENHA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random

jogos = []
quantidade = int(input("Quantos jogos você quer gerar? "))

for i in range(quantidade):
    jogo = sorted(random.sample(range(1, 61), 6))
    jogos.append(jogo)

# Mostrando os jogos gerados
print("\n--- PALPITES GERADOS ---")
for idx, jogo in enumerate(jogos, start=1):
    print(f"Jogo {idx}: {jogo}")

