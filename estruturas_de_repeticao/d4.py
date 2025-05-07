soma = 0
contador = 0

print("Digite as temperaturas em Celsius. Digite -273 para encerrar.")

while True:
    try:
        temp = float(input('Temperatura: '))
        if temp == -273:
            break
        soma += temp
        contador += 1 
    except ValueError:
        print('Valor inválido. Digite uma temperatura numérica.')

if contador > 0 :
    media = soma/contador
    print(f'\nMédia das temperaturas: {media} °C')
else:
    print('\nNenhuma temperatura válida foi informada.')