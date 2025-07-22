# Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
texto = 'TABUADA (DIGITE Nº NEGATIVO PARA SAIR'
print(f'{texto:=^50}')
contador = tabuada = 0
numero = int( input( 'Digite um nº inteiro: ' ) )

while numero >= 0:
    if contador < 10:
        contador += 1
        tabuada = numero * contador
        print(f'{numero} x {contador:2} = {tabuada}')
    elif contador == 10:
        numero = int( input( f'{'Digite outro número inteiro: ':-^40} \n' ) )
        contador = 0
    elif numero < 0:
        break

print('Fim')
