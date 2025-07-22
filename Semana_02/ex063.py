# Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Exemplo: 0 - 1 - 1 - 2 - 3 - 5 - 8 ( o elemento soma com o anterior que resulta no posterior a ele)
texto = 'SEQUENCIA FIBONACCI'
print(f'{texto:=^50}')
t1 = int(input("Digite o primeiro número da sequência: "))
t2 = int(input("Digite o segundo número da sequência: "))
n = int(input("Quantos termos você quer mostrar? "))


contador = 3  # já temos t1 e t2
print("Sequência de Fibonacci a partir do número informado:")
print(f"{t1} → {t2}", end="")

while contador <= n:
    t3 = t1 + t2
    print(f" → {t3}", end="")
    t1 = t2
    t2 = t3
    contador += 1

print(" → FIM")
