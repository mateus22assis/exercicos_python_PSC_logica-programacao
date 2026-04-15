'''5. Faça um programa que leia um vetor com 10 elementos. Em seguida, troque todos os valores negativos do vetor por 0. Imprima o vetor alterado.'''
tamanho_vetor = 3

vetor = [0] * tamanho_vetor

for i in range(tamanho_vetor):
    vetor[i] = int(input(f"Digite o elemento {i+1}: "))

for i in range(tamanho_vetor):
    if vetor[i] < 0:
        vetor[i] = 0

for i in range(tamanho_vetor):
    print(vetor[i])

 
