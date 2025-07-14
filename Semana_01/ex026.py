# Faça um programa que leia uma frase pelo teclado e mostre:
# * quantas vezes aparece a letra "A"
# * em que posição ela aparece a primeira vez
# * em que posição ela aparece a última vez
print('=== DIGITE UMA FRASE ===')
frase = str(input('Digite uma frase: ')).strip().upper()
print(f'''Dentro desta frase digitada ({frase}) a
letra A aparece {frase.count('A')} vezes na frase
aparecendo a primeira vez na posição {frase.find('A')+1} e
aparecendo a ultima vez na posição {frase.rfind('A')}''')
