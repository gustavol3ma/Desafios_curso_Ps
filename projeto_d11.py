l1 = float(input('Informe o lado 1 : '))
l2 = float(input('Informe o lado 2 : '))
l3 = float(input('Informe o lado 3 : '))

if l1 + l2 < l3:
    print('Não formar um triângulo!')
elif l1 == l2 == l3:
    print('Triângulo Equilátero!')
elif l1 == l2 or l2 == l3:
    print('Triãngulo Isósceles!')
elif l1 != l2 != l3 :
    print('triângulo Escaleno!')
