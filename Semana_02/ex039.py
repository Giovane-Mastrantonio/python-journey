# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
#  se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou
#  se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
print('========CONTROLE DE ALISTAMENTO========')
anoNascimento = int(input('Digite o ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento
if idade < 18:
    print(f'Você nasceu em {anoNascimento} e esta com {idade} anos.'
          f'\nFaltam {18 - idade} ano(s) para o alistamento {anoNascimento + 18}.')
elif idade > 18:
    print(f'Você deveria ter se alistado há {idade - 18} ano(s).'
          f'\nSeu alistamento foi em {anoNascimento + 18}.')
else:
    print('Você deve se alistar este Ano!')

print('======TESTANDO O SEXO=======')
sexo = str(input('Digite o sexo (M/F): ')).upper()
if sexo == 'M' and idade < 18:
    print(f'Você nasceu em {anoNascimento} e esta com {idade} anos.'
          f'\nFaltam {18 - idade} ano(s) para o alistamento {anoNascimento + 18}.')
elif sexo == 'M' and idade > 18:
    print(f'Você deveria ter se alistado há {idade - 18} ano(s).'
          f'\nSeu alistamento foi em {anoNascimento + 18}.')
elif sexo == 'M' and idade == 18:
    print('Você deve se alistar este Ano!')
else:
    print('Você não precisa se alistar!')