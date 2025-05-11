temperaturas_mensais = []

for i in range(0,12):
    temperaturas_mensais.append(float(input(f'Digite a média de temperatura do mês {i+1}: ')))

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

media_anual = sum(temperaturas_mensais) / len(temperaturas_mensais)

print('Temperaturas acima da média em: ')
for i in range(0,12):
    if temperaturas_mensais[i]>media_anual:
        print(meses[i])