'''
Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os números primos entre 1 e o número digitado.

'''

numero = int(input('Digite um número inteiro: '))
lista_primos = []


for num in range(2, numero):
  primo = True 
  for teste_divisiveis in range(2, num):
    if num % teste_divisiveis == 0:
      primo = False
      break

  if primo:
    lista_primos.append(num)
print(f'Lista de números primos: {lista_primos}')