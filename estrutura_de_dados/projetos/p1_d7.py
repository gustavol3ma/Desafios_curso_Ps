bactérias_por_dia = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
percentual_de_crescimento_de_bactérias_por_dia = []

for i in range(1, len(bactérias_por_dia)):
    crescimento = 100 * (bactérias_por_dia[i] - bactérias_por_dia[i - 1]) / bactérias_por_dia[i - 1]
    percentual_de_crescimento_de_bactérias_por_dia.append(crescimento)

for i, p in enumerate(percentual_de_crescimento_de_bactérias_por_dia, start=1):
    print(f'Crescimento do dia {i} para o dia {i+1}: {p:.2f}%')
