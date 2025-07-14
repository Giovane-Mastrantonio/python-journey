# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo
# que cada litro de tinta pinta uma área de 2m².
print('=== LÊ ÁREA DE UMA PAREDE E CALCULA LITROS EM TINTA A SER USADO ===')
largura = float(input('Digite sua Largura: '))
altura = float(input('Digite sua Altura: '))
area = largura * altura
litros = area / 2
print('A parede possui {:.2f} m², logo necessitará de {:.2f} litros de tinta'.format(area, litros))