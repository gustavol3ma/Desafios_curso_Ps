numero = int(input('Digite um número interio: '))

if numero <= 1:
    print(f'{numero}não é primo')
else:
    primo = True 
    for i in range(2,int(numero**0.5)+1):
        if numero % i == 0 :
            primo = False
            break
    
    if primo: 
        print(f'{numero} é primo.')
    else:
        print(f'{numero} não é primo.')