#1. Faça um programa que leia um vetor com as notas de 10 alunos e imprima a maior e a menor notas, bem como quais os alunos que obtiveram essas notas (identifique cada aluno pela sua posição no vetor).

tamanho_vetor = 10
notas = [0] * tamanho_vetor


for i in range(tamanho_vetor):
     notas [i] = float(input(f"Digite a nota do aluno {i+1}: "))

maior_nota = notas[0]
menor_nota = notas[0]

for i in range(tamanho_vetor):
     if notas[i] > maior_nota:
          maior_nota = notas[i]   
     if notas[i] < menor_nota:
          menor_nota = notas[i]
          

#mostrando a posiçao
print(f"A maior nota é: {maior_nota}")
print ("Alunos com a maior nota:")
for i in range(tamanho_vetor):
     if notas[i] == maior_nota:
         print(f"Aluno {i+1}")

print(f"A menor nota é: {menor_nota}")
print ("Alunos com a menor nota:")
for i in range(tamanho_vetor):
     if notas[i] == menor_nota:
         print(f"Aluno {i+1}")