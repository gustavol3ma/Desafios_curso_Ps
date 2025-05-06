quantidade_de_litro = float(input('Informe a quantidade de litros vendidos: '))
tipo_com = input('Informe o tipo de combustível\nD - diesel\nE - etanol\n').lower()

#para o etanol
if tipo_com == 'e':
    preco_litro = 1.70
    if quantidade_de_litro <= 15:
        desconto = 0.02
    else:
        desconto = 0.04

    valor_total = quantidade_de_litro * preco_litro
    valor_desconto = desconto * valor_total
    valor_final = valor_total - valor_desconto

    print(f'Desconto: R$ {valor_desconto:.2f}')
    print(f'Preço com desconto: R$ {valor_final:.2f}')

#para o diesel
elif tipo_com == 'd':
    preco_litro = 2.00
    if quantidade_de_litro <= 15:
        desconto = 0.03
    else:
        desconto = 0.05

    valor_total = quantidade_de_litro * preco_litro
    valor_desconto = desconto * valor_total
    valor_final = valor_total - valor_desconto

    print(f'Desconto: R$ {valor_desconto:.2f}')
    print(f'Preço com desconto: R$ {valor_final:.2f}')

else:
    print('Tipo de combustível inválido. Informe "D" para diesel ou "E" para etanol.')
