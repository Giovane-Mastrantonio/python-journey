# Crie um programa que leia o nome completo de uma pessoa e mostre:
# * o nome com todos as letras maiúsculas
# * o nome com todas minúsculas
# * quantas letras ao todo (sem considerar espaços)
# * quantas letras tem o primeiro nome

print('=== DIGITE SEU NOME COMPLETO E FORMATAREMOS E CONTAREMOS OS CARACTERES ===')
nome = str(input('Digite seu nome completo: ')).strip() # já remove espaços
print(f'''Sabendo que seu nome é {nome} vamos:
Transformar tudo em maiusculas: {nome.upper()}
Transformar tudo em minusculas: {nome.lower()}
Contar quantos caracteres tem seu nome: {len(nome) - nome.count(' ')}
Contar quantas letras tem o seu primeiro nome: {nome.find(' ')}''')

