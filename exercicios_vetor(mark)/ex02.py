'''Faça um programa que leia as notas de 10 alunos, calcule a média das notas, e imprima:
A média das notas
Uma listagem contendo os alunos, com suas respectivas notas, que obtiveram notas abaixo da média
Uma listagem contendo os alunos, com suas respectivas notas, que obtiveram notas maiores ou iguais à media
(identifique cada aluno pela sua posição no vetor).
'''
tamanho_vetor = 10

# Usando list comprehension para ler as notas de forma mais concisa
notas = [float(input(f"Digite a nota do aluno {i+1}: ")) for i in range(tamanho_vetor)]

# A função sum() já calcula a soma dos elementos da lista
media = sum(notas) / len(notas)
print(f"A média das notas é: {media}")

print("Alunos com notas acima da média:")
for i, nota in enumerate(notas, start=1):
    if nota >= media:
        print(f"Aluno {i}: Nota {nota}")
print("Alunos com notas abaixo da média:")
for i, nota in enumerate(notas, start=1):
    if nota < media:
        print(f"Aluno {i}: Nota {nota}")
