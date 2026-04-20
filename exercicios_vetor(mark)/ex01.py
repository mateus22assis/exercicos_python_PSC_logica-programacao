#1. Faça um programa que leia um vetor com as notas de 10 alunos e imprima a maior e a menor notas, bem como quais os alunos que obtiveram essas notas (identifique cada aluno pela sua posição no vetor).

tamanho_vetor = 10

notas = [0.0] * tamanho_vetor

for i in range(tamanho_vetor):
    notas[i] = float(input(f"Digite a nota do aluno {i+1}: "))

maior_nota = max(notas)
menor_nota = min(notas)

print(f"\nA maior nota é: {maior_nota}")
print(f"A menor nota é: {menor_nota}")

print("Alunos com a maior nota:")
# enumerate(notas, start=1) já começa a contagem do índice em 1
for i, nota in enumerate(notas, start=1):
     if nota == maior_nota:
         print(f"Aluno {i}")

print("Alunos com a menor nota:")
for i, nota in enumerate(notas, start=1):
     if nota == menor_nota:
         print(f"Aluno {i}")
