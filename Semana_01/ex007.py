# Desenvolva um programa que leia as duas notas de um aluno
# calcule e mostre a sua media
# a linguagem Python permite variáveis com acentuação
print('=== LÊ DUAS NOTAS, CALCULA E MOSTRA A MÉDIA ===')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
média = (nota1 + nota2) / 2
print('As duas notas foram {} e {} e a média é {:.1f}'.format(nota1, nota2, média))
