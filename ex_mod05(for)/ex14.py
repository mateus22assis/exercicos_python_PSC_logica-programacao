contador_masculino_60_80 = 0
contador_feminino_50_70 = 0

print("Por favor, insira o sexo e o peso para 10 pessoas.")

for i in range(10):
    print(f"\nDados para a pessoa {i + 1}:")
    sexo = input("Digite o sexo (M/F): ").upper()
    peso = float(input("Digite o peso em kg: "))

    if sexo == "M" and 60 <= peso <= 80:
        contador_masculino_60_80 += 1
    elif sexo == "F" and 50 <= peso <= 70:
        contador_feminino_50_70 += 1

print(f"\nQuantidade de homens com peso entre 60 e 80 kg: {contador_masculino_60_80}")
print(f"Quantidade de mulheres com peso entre 50 e 70 kg: {contador_feminino_50_70}")