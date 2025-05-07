bacteria_A = 4
bacteria_B = 10 

taxa_A = 0.03
taxa_B = 0.015
dias = 0

while bacteria_A <= bacteria_B:
  bacteria_A *= (1+taxa_A)
  bacteria_B *= (1+taxa_B)
  dias += 1

print(f"A colônia A ultrapassará ou igualará a colônia B em {dias} dias.")