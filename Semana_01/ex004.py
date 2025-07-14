# faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possíveis sobre ele
# experimento os is como print(n.isnumeric()) depois de um input
# METODO isnumeric, isupper, isspace, ..., só pode ser utilizado com Strings

a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um numeral? ', a.isnumeric())
print('É imprimível? ', a.isprintable())
print('É caixa alta? ', a.isupper())
print('É um alfanumérico? ', a.isalnum())
print('É um digito? ', a.isdigit())



