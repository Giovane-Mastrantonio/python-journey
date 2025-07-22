# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar [ 2 ] multiplicar [ 3 ] maior [ 4 ] novos números [ 5 ] sair do programa
# [ 4 ] novos números => você irá digitar outros dois números e voltar ao menu
# Seu programa deverá realizar a operação solicitada em cada caso.
texto = 'LÊ DOIS VALORES COM OPÇOES DE AÇÃO'
print(f'{texto:=^50}')
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
menu = 0
while menu != 5:
    print('--X' * 10)
    print('Digite:'
          '\n[ 1 ] somar'
          '\n[ 2 ] multiplicar'
          '\n[ 3 ] maior'
          '\n[ 4 ] novos números'
          '\n[ 5 ] sair do programa' )
    menu = int(input('\nQual sua escolha: '))
    print( '--X' * 10 )

    if menu == 1:
        print('Você escolheu SOMAR...\n')
        print(f'Os dois valores {valor1} e {valor2} somados é igual a \033[1;33;40m  {valor1 + valor2}  \033[m ')

    elif menu == 2:
        print('Você escolheu MULTIPLICAR...\n')
        print(f'Os dosi valores {valor1} e {valor2} multiplicados é igual a \033[1;33;40m  {valor1 * valor2}  \033[m ')

    elif menu == 3:
        maior = valor1 if valor1 > valor2 else valor2
        print('Você escolheu infomar o MAIOR...\n')
        print(f'O maior valor entre {valor1} e {valor2} é o \033[1;33;40m  {maior}  \033[m ')

    elif menu == 4:
        print('Você escolheu TROCAR os números...\n')
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))

    elif menu == 5:
        print('Saindo do programa...')
    else:
        print('Opção inválida. Tente novamente.')
