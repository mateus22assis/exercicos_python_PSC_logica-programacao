'''Faça um programa que leia as notas de 10 alunos, calcule a média das notas, e imprima:
A média das notas
Uma listagem contendo os alunos, com suas respectivas notas, que obtiveram notas abaixo da média
Uma listagem contendo os alunos, com suas respectivas notas, que obtiveram notas maiores ou iguais à media
(identifique cada aluno pela sua posição no vetor).
'''
tamanho_vetor = 3

notas = []
soma = 0


for i in range(tamanho_vetor):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    notas.append(nota)
    soma += nota

media = soma / tamanho_vetor
print(f"A média das notas é: {media}")

print("Alunos com notas acima da média:")
for i in range(tamanho_vetor):
    if notas[i] >= media:
        print(f"Aluno {i+1}: Nota {notas[i]}")
        
print("Alunos com notas abaixo da média:")
for i in range(tamanho_vetor):
    if notas[i] <10 media:
        print(f"Aluno {i+1}: Nota {notas[i]}")