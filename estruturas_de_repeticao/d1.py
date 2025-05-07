n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

inicio = min(n1, n2)
fim = max(n1, n2)

print(f'Intervalo entre {inicio} e {fim}:')
for i in range(inicio, fim + 1):
    print(i)