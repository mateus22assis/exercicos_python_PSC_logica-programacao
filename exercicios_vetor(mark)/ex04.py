''' Faça um programa que leia dois vetores com 10 elementos cada um. Utilize outros dois vetores que recebam o resultado da multiplicação e divisão dos elementos de mesmo índice do primeiro vetor pelo segundo. Imprima em seguida os 4 vetores.'''

tamanho_vetor = 10

vetor1 = [int(input(f"Vetor 1 - Pos {i+1}: ")) for i in range(tamanho_vetor)]
vetor2 = [int(input(f"Vetor 2 - Pos {i+1}: ")) for i in range(tamanho_vetor)]

vetor_multiplicacao = [vetor1[i] * vetor2[i] for i in range(tamanho_vetor)]
vetor_divisao = [vetor1[i] / vetor2[i] if vetor2[i] != 0 else 0 for i in range(tamanho_vetor)]

print("Vetor 1:", vetor1)
print("Vetor 2:", vetor2)
print("Vetor da Multiplicação:", vetor_multiplicacao)
print("Vetor da Divisão:", vetor_divisao)
