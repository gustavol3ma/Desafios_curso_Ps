notas = []

for i in range(15):
    while True:
        try:
            nota = float(input(f'Digite uma nota {i+1} de 0 ate 5 : '))
            if 0 <= nota <=5:
                notas.append(nota)
                break
            else:
                print('Nota inválida .Digite um valor entre 0 e 5.')
        except ValueError:
            print('Entrada inválida')
