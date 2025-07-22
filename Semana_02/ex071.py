# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
texto = 'SIMULADOR DE CAIXA ELETRÔNICO'
print(f'{texto:=^50}\n')
print("=" * 40)
print("{:^40}".format("CAIXA ELETRÔNICO"))
print("=" * 40)

valor = int(input("Qual valor você quer sacar? R$ "))
total = valor
cedula = 50
quantidade = 0

while True:
    if total >= cedula:
        total -= cedula
        quantidade += 1
    else:
        if quantidade > 0:
            print(f"Total de {quantidade} cédula(s) de R${cedula}")
        # Troca para a próxima cédula
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        quantidade = 0
        if total == 0:
            break

print("=" * 40)
print("Volte sempre ao nosso banco!")
print("=" * 40)
