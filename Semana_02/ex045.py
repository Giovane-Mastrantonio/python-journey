# Crie um programa que faça o computador jogar Jokenpô com você (Pedra, papel e tesoura)
# Lembrando que são 3 elementos com dois jogadores, totalizando 9 combinações
# sorteando para o computador => random.choice(seq)
from random import choice # Irá sortear para o computador
from time import sleep # Irá aguardar um tempo simulando jogar
texto = 'JOGANDO JOKENPÔ (PEDRA, PAPEL E TESOURA)'
print(f'{texto:=^50}')
escolhaDoJogador = int(input('Escolha um elemento'
                             '\n[1] PEDRA'
                             '\n[2] PAPEL'
                             '\n[3] TESOURA'
                             '\n Digite: '))

escolhaDoSistema = choice(['PEDRA', 'PAPEL', 'TESOURA'])
print('JOoo...')
sleep(2)
print('KEN')
sleep(1)
print('PÔ!')
sleep(1)
if escolhaDoJogador == 1:
    if escolhaDoSistema == 'TESOURA':
     print('você PEDRA e computador TESOURA'
          '\nVocê GANHOU!')
    elif escolhaDoSistema == 'PAPEL':
        print('você PEDRA e computador PAPEL'
              '\nVocê PERDEU!')
    else:
        print('você PEDRA e computador PEDRA'
              '\nIMPATOU!')


elif escolhaDoJogador == 2:
    if escolhaDoSistema == 'TESOURA':
     print('você PAPEL e computador TESOURA'
          '\nVocê PERDEU!')
    elif escolhaDoSistema == 'PAPEL':
        print('você PAPEL e computador PAPEL'
              '\nIMPATOU!')
    else:
        print('você PAPEL e computador PEDRA'
              '\nVocê GANHOU!')

elif escolhaDoJogador == 3:
    if escolhaDoSistema == 'TESOURA':
     print('você TESOURA e computador TESOURA'
          '\nIMPATOU!')
    elif escolhaDoSistema == 'PAPEL':
        print('você TESOURA e computador PAPEL'
              '\nVocê GANHOU!')
    else:
        print('você TESOURA e computador PEDRA'
              '\nVocê PERDEU!')

else:
    print('Valor digitado incorreto!')
