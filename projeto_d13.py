vendas2022 = float(input('informe o valor da quantidade de vendas em 2022 : '))
vendas2023 = float(input('informe o valor da quantidade de vendas em 2023 : '))

variacao = (vendas2023 - vendas2022 / vendas2022)*100

if variacao > 20 :
    print("Sugestão: Bonificação para o time de vendas.")
elif 2 < variacao <= 20:
    print("Sugestão: Pequena bonificação para o time de vendas.")
elif -10 <= variacao <= 2:
    print("Sugestão: Planejamento de políticas de incentivo às vendas.")
else: 
    print("Sugestão: Corte de gastos.")