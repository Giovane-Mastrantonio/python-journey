# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar
# mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
texto = 'MOSTRANDO OS 10 PRIMEIROS TERMOS DE UMA PA'
print(f'{texto:=^50}')
primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
termo = primeiro
contador = 1
total = 0
mais = 10  # começa mostrando 10 termos

while mais != 0:
    total += mais
    while contador <= total:
        print(f"{termo}", end=" → ")
        termo += razao
        contador += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? (Digite 0 para sair): "))
print(f"Progressão finalizada com {total} termos mostrados.")
