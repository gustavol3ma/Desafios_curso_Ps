dados = { 
    'Área Norte': [2819, 7236],
    'Área Leste': [1440, 9492],
    'Área Sul': [5969, 7496],
    'Área Oeste': [14446, 49688],
    'Área Centro': [22558, 45148]
}

soma_media = 0
maior_diversidade = ''
maior_soma = 0

for area, especies in dados.items():
    soma_especies = sum(especies)
    media = soma_especies / len(especies)  # corrigido
    print(f'A {area} tem a média de {media:.2f} espécies')

    soma_media += media  # corrigido

    if soma_especies > maior_soma:
        maior_soma = soma_especies
        maior_diversidade = area

media_total = soma_media / len(dados)

print(f'\nMédia geral de espécies: {media_total:.2f}')
print(f'Área com a maior diversidade biológica: {maior_diversidade}')
