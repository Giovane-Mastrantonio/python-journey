# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais – ISÓSCELES: dois lados iguais
# – ESCALENO: todos os lados diferentes
print('=========TEOREMA DA DESIGUALDADE TRIANGULAR============')
reta_a = float(input('Digite o valor da reta a: '))
reta_b = float(input('Digite o valor da reta b: '))
reta_c = float(input('Digite o valor da reta c: '))

if reta_a + reta_b > reta_c and reta_b + reta_c > reta_a and reta_c + reta_a > reta_b:
    if reta_a == reta_b == reta_c:
       print('As retas formam um triangulo EQUILATERO')
    elif reta_a != reta_b != reta_c != reta_a:
       print('As retas formam um triangulo ESCALENO')
    else:
       print('As retas formam um triangulo ISÓCELES')
else:
     print('As retas não podem formar um triangulo')