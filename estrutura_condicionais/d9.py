numero_str = input("Digite um número: ")

try:
    numero = float(numero_str)
    if numero.is_integer():
        print("O número é inteiro.")
    else:
        print("O número é decimal.")
except ValueError:
    print("Entrada inválida. Por favor, digite um número válido.")
