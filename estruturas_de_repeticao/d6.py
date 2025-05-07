while True:
    try:
        numero = int(input('Digite um número interio de 1 a 10 : '))
        if 1 <= numero <= 10 :
            break
        else:
            print("Número fora do intervalo. Digite um valor de 1 a 10.")
    except ValueError:
         print("Entrada inválida. Digite um número inteiro.")

print(f'\nTabuada do {numero}:')
for i in range(1,11):
    resultado = numero * i 
    print(f'{numero}x{i} = {resultado}')
