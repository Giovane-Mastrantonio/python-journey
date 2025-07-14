# O mesmo professor do desafio anterior quer sortear a ordem de
# apresentação de trabalhos dos alunos. Faça um programa que leia
# o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle
print('=== DIGITE O NOME DOS ALUNOS PARA O SORTEIO DA APRESENTAÇÃO ===')
nome = []
for i in range(4):
    aluno = input(f'Digite o nome do {i + 1}º aluno: ')
    nome.append(aluno)

shuffle(nome) #embaralha a lista

print('\n--- ORDEM DE APRESENTAÇÃO ---')
for posicao, nome in enumerate(nome, start=1):
    print(f'{posicao}º - {nome}')