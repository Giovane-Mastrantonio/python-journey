# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso;
# Entre 18,5 e 25: Peso Ideal
# 25,0 até 30: sobrepeso;
# 30,0 até 40: obesidade;
# acima de 40,0: obesidade grau III (mórbida)
# IMC = Peso ÷ (Altura × Altura)   CÁLCULO => IMC = 80 kg ÷ (1,80 m × 1,80 m) = 24,69 kg/m2 (Peso ideal)
print('=====CALCULANDO O INDICE DE MASSA CORPORAL (IMC)======')
peso = float(input('Digite o valor do peso: (Kg) '))
altura = float(input('Digite o valor da altura: (m) '))
imc = peso / (altura * altura)

if imc < 18.5:
    print(f'Você está pesando {peso} classificado como ABAIXO do peso.')
elif 18.5 <= imc < 25:
    print(f'Você está pesando {peso} classificado como peso IDEAL.')
elif 25 <= imc < 30:
    print(f'Você está pesando {peso} classificado como SOBREPESO.')
elif 30 <= imc < 40:
    print(f'Você está pesando {peso} classificado como OBESIDADE.')
else:
    print(f'Você está pesando {peso} classificado como OBESIDADE grau III.')
