# Confederação Nacional de Natação precisa de um programa que leia
# o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR – Até 25 anos: SÊNIOR – Acima de 25 anos: MASTER
from datetime import date

print('======CATEGORIAS DE NATAÇÃO=========')
anoNascimento = int(input('Digite o ano de nascimento: '))
atual = date.today().year
idade = atual - anoNascimento
print('=' * 30)

if idade <= 9:
        print(f' Você tem {idade} anos.'
              f'\n Vai para a Categoria MIRIM')
elif idade <= 14:
        print(f' Você tem {idade} anos.'
              f'\n Vai para a Categoria INFANTIL')
elif idade <= 19:
        print(f' Você tem {idade} anos.'
              f'\n Vai para a Categoria JÚNIOR')
elif idade <= 25:
        print(f' Você tem {idade} anos.'
              f'\n Vai para a Categoria SÊNIOR')
else:
        print(f' Você tem {idade} anos.'
              f'\n Vai para a Categoria MASTER')
