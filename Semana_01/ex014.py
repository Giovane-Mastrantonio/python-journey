#Lé uma temperatura em Celsius e converte ela para Fahrenheit
print('=== DIGITE A TEMPERATURA EM CELSIUS QUE CONVERTEREMOS EM FAHRENHEIT ===')
celsius = float(input('Insira a temperatura: '))
fahrenheit = (celsius * 9) / 5 + 32
print('A temperatura de {}°C corresponde a {}°F'.format(celsius, fahrenheit))