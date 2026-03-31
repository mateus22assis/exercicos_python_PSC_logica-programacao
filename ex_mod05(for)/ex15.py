print("Calculadora de Média para 3 Alunos")

for i in range(1, 4): # Loop para os 3 alunos (i+1 para mostrar Aluno 1, 2, 3)
    print(f"\n--- Aluno {i} ---")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    
    media = (nota1 + nota2) / 2
    
    print(f"A média do Aluno {i} é: {media:.2f}") # Formata a média com 2 casas decimais