# escreva um programa que leia um valor em metros e o exiba
# convertido em centimetros e milimetros
print('=== DIGITE VALOR EM METROS QUE CONVERTEREMOS EM CM E MM ===')
metros = float(input('Digite em Metros: '))
cm = metros * 10
mm = metros * 100
print('O valor em metros é {} em centímetros corresponde a {} e em milímetros em {}'.format(metros, cm, mm))

print('=== BONUS CONVERTER E MOSTRAR EM KM HM DAM M DM CM MM ===')
dam = metros / 10
hm = dam / 10
km = hm / 10
dm = metros * 10
cm = dm * 10
mm = cm * 10
print('{6} Metro = {2} Quilômetro'
      '\n{6} Metro  = {1} Hectômetro'
      '\n{6} Metro = {0} Decâmetro'
      '\n\033[1m>>Metro\033[0m = {6} metro'
      '\n{6} Metro = {3} Decímetro'
      '\n{6} Metro = {4} Centimetro'
      '\n{6} Metro = {5} Milímetro'.format(dam, hm, km, dm, cm, mm,metros))

