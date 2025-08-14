# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
# MODELO: Na palavra APRENDER temos as vogais a e e
texto = 'MOSTRANDO VOGAIS'
print(f'{texto:=^50}')

# Tupla com várias palavras (sem acentos)
palavras = (
    'aprender', 'programar', 'python', 'mercado', 'programador', 'gratis', 'trabalhador',
    'trabalho', 'futuro', 'oportunidade', 'sucesso'
)

vogais = 'aeiou'

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in vogais:
            print(letra, end=' ')
