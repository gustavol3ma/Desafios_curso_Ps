letra = input("Digite uma letra : ").lower()

if len(letra) == 1 and letra:
    
    if letra in 'aeiou':
        print('É uma vogal!')
    else: 
        print('É uma consoante!')
