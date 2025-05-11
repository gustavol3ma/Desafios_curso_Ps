dados_vendas = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60, 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}

total_vendas =  0
produto_mais_vendido = ''
unidades_produtos_mais_vendido = 0

for produto in dados_vendas.keys():
    total_vendas += dados_vendas[produto]
    if dados_vendas[produto]>unidades_produtos_mais_vendido:
        unidades_produtos_mais_vendido = dados_vendas[produto]
        produto_mais_vendido = produto

print(f'Total de vendas é {total_vendas}')
print(f'{produto_mais_vendido} é o mais vendido')