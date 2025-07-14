# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
# EX: Ana Maria de Souza
# primeiro = Ana
# último = Souza
print('=== DIGITE SEU NOME COMPLETO ===')
nome = input('Digite seu nome: ').strip()
nome = nome.split()
print(f'''O primeiro nome é {nome[0]} e o
último nome é {nome[-1]}''')
