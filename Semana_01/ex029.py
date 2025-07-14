# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80 Km/h, mostre uma mensagem dizendo
# que ele foi multado.
# A multa vai custar R$ 7.00 por cada Km acima do limite
print('===== DIGITE A VELOCIDADE DO CARRO =====')
velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f' Você vai pagar R${multa:.2f} de multa!')

print(' BOA VIAGEM ')
