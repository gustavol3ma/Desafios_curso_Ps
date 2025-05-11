dados = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
        'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
        'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
        'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

total_idades = 0

for setor, idades in dados.items():

  media_idade = sum(idades) / len(idades)

  print(f'O {setor} tem a média de {media_idade}')

  total_idades += sum(idades)

media_total = total_idades / (len(idades) * len(dados))
print(f'A média de idade geral é {media_total}')

acima_media = 0
for setor, idades in dados.items():
  for id in idades:
    if id > media_total:
      acima_media += 1

print(f'{acima_media} pessoas estão acima da idade média geral')