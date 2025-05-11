salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]

dic_abonos = {}
total_abono = 0
abonos_minimo = 0 
maior_abono = 0

for salario in salarios:
    abono = salario*0.1
    if abono < 200:
        abono = 200
    dic_abonos[salario] = abono

for abono in dic_abonos.values():
    if abono == 200:
        abonos_minimo += 1 
    if abono > maior_abono:
        maior_abono= abono
    total_abono += abono

print(f'Abonos: {dic_abonos}')
print(f'Total de gasto com abonos: {total_abono}')
print(f'Número de funcionários que receberam o abono mínimo: {abonos_minimo}')
print(f'Maior valor de abono: {maior_abono}')