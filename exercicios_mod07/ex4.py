''' Faça um programa que leia dois vetores com 10 elementos cada um. Utilize outros dois vetores que recebam o resultado da multiplicação e divisão dos elementos de mesmo índice do primeiro vetor pelo segundo. Imprima em seguida os 4 vetores.'''
tamanho_vetor = 3

vetor1 = [0] * tamanho_vetor 
vetor2 = [0] * tamanho_vetor 

for i in range(tamanho_vetor):
    vetor1[i] = int(input(f"Digite o elemento {i+1} do primeiro vetor: "))
for i in range(tamanho_vetor):
    vetor2[i] = int(input(f"Digite o elemento {i+1} do segundo vetor: "))

vetor_multiplicacao = [0] * tamanho_vetor
vetor_divisao = [0] * tamanho_vetor 

for i in range(tamanho_vetor):
    vetor_multiplicacao[i] = vetor1[i] * vetor2[i]
    if vetor2[i] != 0:
        vetor_divisao[i] = vetor1[i] / vetor2[i]
    else:
        vetor_divisao[i] = "Divisão por zero"

print("Vetor 1:", vetor1)
print("Vetor 2:", vetor2)
print("Vetor da Multiplicação:", vetor_multiplicacao)
print(f"Vetor da Divisão: {vetor_divisao}")

