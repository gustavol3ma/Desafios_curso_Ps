
faixa_1 = 0  
faixa_2 = 0  
faixa_3 = 0  
faixa_4 = 0  

print("Digite as idades dos pensionistas.\nDigite um número negativo para encerrar.")

while True:
    try:
        idade = int(input("Idade: "))
        if idade < 0:
            break
        elif 0 <= idade <= 25:
            faixa_1 += 1
        elif 26 <= idade <= 50:
            faixa_2 += 1
        elif 51 <= idade <= 75:
            faixa_3 += 1
        elif 76 <= idade <= 100:
            faixa_4 += 1
        else:
            print("Idade fora do intervalo de 0 a 100. Ignorada.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")


print("\nDistribuição de idades:")
print(f"[  0 - 25]: {faixa_1} pessoas")
print(f"[ 26 - 50]: {faixa_2} pessoas")
print(f"[ 51 - 75]: {faixa_3} pessoas")
print(f"[ 76 -100]: {faixa_4} pessoas")
