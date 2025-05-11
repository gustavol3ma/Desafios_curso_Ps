'''
Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao total de compras.

'''

gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

total_de_compra_acima3000 = 0 

for i in gastos:
    if i > 3000:
        total_de_compra_acima3000 += 1

quantidades_de_compras = len(gastos)

porcentagem_das_compras = 100*(total_de_compra_acima3000)/quantidades_de_compras

print(f'{total_de_compra_acima3000} compras foram acima de R$3000,00.')
print(f'{porcentagem_das_compras}% dos gastos foram acima de R$3000,00.')