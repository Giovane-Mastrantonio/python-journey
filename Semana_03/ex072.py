# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
# se não estiver entre 0 e 20 deve repetir o comando (tente novamente)

texto = 'TUPLA DE 0 A 20 POR EXTENSO'
print(f'{texto:=^50}')

# Tupla com os números por extenso de 0 a 20
numeros = (
    'zero', 'um', 'dois', 'três', 'quatro',
    'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze', 'quatorze',
    'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove',
    'vinte'
)

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {numeros[num]}.')
        break
    else:
        print('Tente novamente. ', end='')
