# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
texto = 'MOSTRANDO OS 10 PRIMEIROS TERMOS DE UMA PA'
print(f'{texto:=^50}')
primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
print("\nOs 10 primeiros termos da PA são:")
termo = primeiro
contador = 1
while contador <= 10:
    print(termo, end=" → ")
    termo += razao
    contador += 1
print("FIM")
