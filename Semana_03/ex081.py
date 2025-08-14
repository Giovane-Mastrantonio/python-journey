# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
texto = 'LÊ VARIOS NºS E VERIFICA'
print(f'{texto:=^50}')
numeros = []

while True:
    entrada = input('Digite um número (ou "sair" para encerrar): ').strip().lower()
    if entrada == 'sair':
        break  # Sai do loop se o usuário digitar sair
    # Tenta converter para inteiro
    try:
        n = int(entrada)
        numeros.append(n)
    except ValueError:
        print('Entrada inválida! Digite um número ou "sair".')

# A) Quantos números foram digitados
quantidade = len(numeros)

# B) Lista em ordem decrescente
numeros_decrescente = sorted(numeros, reverse=True)

# C) Verificar se o número 5 está na lista
tem_cinco = 5 in numeros

# Mostrando os resultados
print('▬' * 30)
print(f'Você digitou {quantidade} números.')
print(f'A lista de valores em ordem decrescente é: {numeros_decrescente}')
if tem_cinco:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 NÃO foi encontrado na lista.')
