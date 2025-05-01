per_crecismento = {}

for ano in [2023,2024,2025]:
    while True:
        try:
            per_c = float(input(f'Informe o percentual de crescimento no ano de {ano} : '))
            per_crecismento[ano] = per_c
            break
        except ValueError:
            print('Número inválido ')

melhor_ano = None
maior_valor = -float('inf') #vai começar pelo maior valor 

for ano in per_crecismento:
    if per_crecismento[ano] > maior_valor:
        maior_valor = per_crecismento[ano]
        melhor_ano = ano

pior_ano = None
menor_valor = float('inf')

for ano in per_crecismento:
    if per_crecismento[ano]<menor_valor:
        menor_valor = per_crecismento[ano]
        pior_ano = ano


print('=======MURAL======')
print('O maior valor foi ',maior_valor)
print('O melhor ano foi ',melhor_ano)
print('O pior valor foi ',menor_valor)
print('O pior ano  foi ',pior_ano)