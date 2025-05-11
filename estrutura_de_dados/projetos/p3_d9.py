resposta = []
gabarito = ['d', 'a', 'c', 'b', 'a', 'd', 'c', 'c', 'a', 'b']
nota = 0

for i in range(0,10):
    resposta.append(input(f'Insira a resposta da questão {i+1}: ').lower())
    #Eu usei a função lower para garantir que o usuário coloque tanto letra Ma. como Mi.

for i in range(0,10):

    if resposta[i] == gabarito [i]:
        nota += 1

if nota > 7:
    print(f'Nota final: {nota}')
    print('Aprovado!')
else:
    print(f'Nota final: {nota}')
    print('Reprovado!')