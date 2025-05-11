ids = []
doce = 0
amargo = 0

for i in range(0,10):
    ids.append(int(input(f'Digite o {i+1}° ID : ')))

for id in ids:
    if id % 2 == 0 :
        doce += 1 
    else:
        amargo += 1

print(f'Quantidade de produtos doces: {doce}')
print(f'Quantidade de produtos amargos: {amargo}')