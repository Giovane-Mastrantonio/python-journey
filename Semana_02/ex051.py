# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
# Solicita ao usuário o primeiro termo e a razão da PA
texto = 'MOSTRANDO OS 10 PRIMEIROS TERMOS DE UMA PA'
print(f'{texto:=^50}')
primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
print("Os 10 primeiros termos da PA são:")

for i in range(0, 10):
    termo = primeiro + i * razao
    print(termo, end=" -> ")

print("FIM")


