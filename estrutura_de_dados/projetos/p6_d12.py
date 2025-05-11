votos = {'Design 1': 1334, 'Design 2': 982, 'Design 3': 1751, 'Design 4': 210, 'Design 5': 1811}

total_voto = 0
vencedor = 0 
voto_vencedor = 0

for design , voto_design in votos.items():
    total_voto += voto_design
    if voto_design > voto_vencedor:
        voto_vencedor = voto_design
        vencedor = design

porcentagem = 100*(voto_vencedor) / total_voto

print(f'{vencedor} é o vencedor: ')
print(f'Porcentagem de votos: {porcentagem}%')
