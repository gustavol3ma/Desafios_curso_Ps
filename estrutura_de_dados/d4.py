'''
 Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.

'''
lista_numeros = []

for i in range(0,5):
    n = int(input('Digite um número interio: '))
    lista_numeros.append(n)

print(f'Lista de números inserido inversa: {lista_numeros[::-1]}')