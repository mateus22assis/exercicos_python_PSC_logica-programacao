# Programa que recebe a idade e o peso de sete pessoas, calcula a média das idades e a quantidade de pessoas com mais de 90 kg.
quantidade_mais_90kg = 0
soma_idades = 0

print("Por favor, digite a idade e o peso de sete pessoas:")

for i in range(1, 8):
    print(f"\n--- Pessoa {i} ---")
    idade = int(input("Digite a idade: "))
    peso = float(input("Digite o peso (em kg): "))

    soma_idades += idade

    if peso > 90:
        quantidade_mais_90kg += 1

media_idades = soma_idades / 7

print(f"\n--- Resultados ---")
print(f"Quantidade de pessoas com mais de 90 kg: {quantidade_mais_90kg}")
print(f"Média das idades das sete pessoas: {media_idades:.2f}")