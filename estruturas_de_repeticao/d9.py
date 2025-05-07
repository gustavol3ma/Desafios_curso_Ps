# Inicializando os contadores
c1 = c2 = c3 = c4 = nulos = brancos = 0
total_votos = 0

print("ELEIÇÃO PARA GERÊNCIA")
print("1 - Candidato(a) 1")
print("2 - Candidato(a) 2")
print("3 - Candidato(a) 3")
print("4 - Candidato(a) 4")
print("5 - Voto NULO")
print("6 - Voto em BRANCO")

# Loop para 20 colaboradores
for i in range(1, 21):
    while True:
        try:
            voto = int(input(f"Colaborador(a) {i}, digite seu voto (1-6): "))
            if voto in [1, 2, 3, 4, 5, 6]:
                total_votos += 1
                if voto == 1:
                    c1 += 1
                elif voto == 2:
                    c2 += 1
                elif voto == 3:
                    c3 += 1
                elif voto == 4:
                    c4 += 1
                elif voto == 5:
                    nulos += 1
                elif voto == 6:
                    brancos += 1
                break
            else:
                print("Voto inválido. Digite um número entre 1 e 6.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

# Exibindo resultados
print("\nRESULTADO DA ELEIÇÃO:")
print(f"Candidato(a) 1: {c1} votos")
print(f"Candidato(a) 2: {c2} votos")
print(f"Candidato(a) 3: {c3} votos")
print(f"Candidato(a) 4: {c4} votos")
print(f"Votos nulos: {nulos}")
print(f"Votos em branco: {brancos}")

# Porcentagens
porc_nulos = (nulos / total_votos) * 100
porc_brancos = (brancos / total_votos) * 100

print(f"\nPorcentagem de votos nulos: {porc_nulos:.2f}%")
print(f"Porcentagem de votos em branco: {porc_brancos:.2f}%")


candidatos = [c1, c2, c3, c4]
mais_votado = max(candidatos)
if candidatos.count(mais_votado) > 1:
    print("\nHouve empate entre os(as) candidatos(as) mais votados(as).")
else:
    vencedor = candidatos.index(mais_votado) + 1
    print(f"\nO(A) vencedor(a) da eleição foi o(a) candidato(a) {vencedor} com {mais_votado} votos.")
