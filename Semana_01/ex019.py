# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o
# nome do escolhido.
# Ver biblioteca randon

from random import choice
print('=== DIGITE O NOME DE 4 ALUNOS E SORTEAREMOS UM ===')

nome = []

for i in range(4):
    aluno = input(f'Digite o nome do {i + 1}º aluno: ')
    nome.append(aluno)

sorteado = choice(nome)
print(f'O aluno sorteado foi {sorteado}')
