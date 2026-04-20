'''5. Faça um programa que leia um vetor com 10 elementos. Em seguida, troque todos os valores negativos do vetor por 0. Imprima o vetor alterado.'''

tamnho_vetor = 10
vetor = [int(input(f"Digite o elemento {i+1}: ")) for i in range(10)]

for i in range(tamnho_vetor):
    if vetor[i] < 0:
        vetor[i] = 0

print("Vetor alterado:", vetor)

