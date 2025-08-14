# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e
# os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
texto = 'CRIANDO LISTAS'
print(f'{texto:=^50}')
# Listas principais
todos = []
pares = []
impares = []

while True:
    entrada = input('Digite um número (ou digite "sair" para encerrar): ').strip().lower()
    if entrada == 'sair':
        break
    try:
        n = int(entrada)
        todos.append(n)
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    except ValueError:
        print('Entrada inválida! Digite um número ou "sair".')

# Exibindo resultados
print('▬' * 30)
print(f'A lista completa é {todos}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
