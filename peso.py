peso = []

for num in range (5):
    kg = float(input("Digite o peso: "))
    peso.append(kg)

peso_b = sorted(peso)

print(f"O menor peso foi ", peso_b[0], "e o maior peso foi", peso_b[4])