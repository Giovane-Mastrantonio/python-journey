# Desenvolva um programa que leia o comprimento de três retas e
# diga ao usuário se elas podem ou não formar um triangulo
# a condição matemática para isso tem o nome de Teorema da desigualdade triangular
# Para três segmentos a, b e c formarem um triângulo, a soma de dois lados deve ser sempre maior que o terceiro:
print('TEOREMA DA DESIGUALDADE TRIANGULAR')
reta_a = float(input('Digite o valor da reta a: '))
reta_b = float(input('Digite o valor da reta b: '))
reta_c = float(input('Digite o valor da reta c: '))
if reta_a + reta_b > reta_c and reta_b + reta_c > reta_a and reta_c + reta_a > reta_b:
    print('Os valores acima podem formar um triangulo')
else:
    print('As retas não podem formar um triangulo')
