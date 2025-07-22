# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
texto = 'MOSTRANDO MÉDIA, MAIOR E MENOR'
print(f'{texto:=^50}')
soma = 0
contador = 0
maior = None
menor = None

while True:
    numero = int(input("Digite um número inteiro: "))
    soma += numero
    contador += 1
                        # Atualiza maior e menor
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

                        # Pergunta se quer continuar
    opcao = input("Quer continuar? [S/N]: ").strip().upper()
    if opcao == 'N':
        break

                        # Calcula a média
media = soma / contador if contador > 0 else 0

                        # Exibe resultados
print(f"\nVocê digitou {contador} números.")
print(f"A média dos valores é {media:.2f}.")
print(f"O maior valor foi {maior} e o menor valor foi {menor}.")
