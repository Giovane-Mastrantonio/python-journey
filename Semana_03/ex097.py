# Faça um programa que tenha uma função chamada escreva(), que receba um texto
# qualquer como parâmetro e mostre uma mensagem com tamanho adaptável das linhas superiores e inferiores.
texto = 'FUNÇÃO ESCREVA'
print(f'{texto:=^50}')

def escreva(mensagem):
    tamanho = len( mensagem )
    linha_borda = '~' * tamanho

    print( linha_borda )
    print( mensagem )
    print( linha_borda )

escreva( 'Curso de Python no YouTube' )
escreva( 'Oi' )
escreva( 'Python' )
escreva( 'Programação' )
escreva( 'Olá, mundo!' )



