num = int(input('Informe um número inteiro : '))
ope =int(input('Digite 1 se deseja saber se o número é par ou ímpar \nDigite 2 se deseja saber se o número é positivo ou negativo \nDigite 3 se deseja saber se o número é inteiro ou decimal\n'))

if ope == 1:
    if num%2:
        print('O número é par')
    else:
        print('O número é ímpar')

elif ope == 2:
    if num >= 0:
        print('O número é positivo')
    else:
        print('O número é negativo')

elif ope == 3:
    numf = float(num)
    if numf.is_integer():
        print('Número inteiro')
    else:
        print('Número é decimal')

