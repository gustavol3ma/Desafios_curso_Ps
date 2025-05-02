turno = input('Qual turno você estuda ?').lower()

if turno == 'manhã':
    print('Bom dia!')
elif turno == 'tarde':
    print('Boa tarde!')
elif turno == 'noite':
    print('Boa noite!')
else:
    print('Valor inválido!')
    print('Veja se você colocou alguma letra errada ou algum espaço')
