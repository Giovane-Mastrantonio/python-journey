# Melhore o jogo onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
#  mostrando no final quantos palpites foram necessários para vencer.
import random

texto = 'ADIVINHAR DE 0 A 10 NÚMERO SORTEADO'
print(f'{texto:=^50}')

# sorteia um número de 0 a 10
n = random.randint(0, 10)

contador = 0
nusuario = int(input('Digite seu número da sorte de 0 a 10: '))

# enquanto não acertar, continua
while nusuario != n:
    contador += 1
    texto2 = [
        'Ainda não deu, tente novamente: ',
        'Quase lá, vamos de novo: ',
        'Sinto que está perto, mais uma: ',
        'Não desista, tente novamente: '   ]
    sorteiaTexto = random.choice(texto2)
    nusuario = int(input(sorteiaTexto))
# quando sair do while é porque acertou
contador += 1
if contador == 1:
    print(f'Você VENCEU!! \nUtilizou {contador} tentativa.')
else:
    print(f'Você VENCEU!! \nUtilizou {contador} tentativas.')


