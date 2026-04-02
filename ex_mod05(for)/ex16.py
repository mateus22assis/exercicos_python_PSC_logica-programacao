#prgrama que recebe e indentifica maior e menor nota de 5 alunos
maior_nota = float('-inf') # Inicializa com um valor muito baixo
menor_nota = float('inf')  # Inicializa com um valor muito alto

print("Por favor, digite as notas de 5 alunos:")

for i in range(1, 6):
    nota = float(input(f"Digite a nota do aluno {i}: "))

    if nota > maior_nota:
        maior_nota = nota
    if nota < menor_nota:
        menor_nota = nota

print(f"\nA maior nota informada foi: {maior_nota:.2f}")
print(f"A menor nota informada foi: {menor_nota:.2f}")