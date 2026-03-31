
matricula = int(input("Digite a matrícula do aluno (número negativo para sair): "))


while matricula >= 0: 
   
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    nota3 = float(input("Digite a terceira nota do aluno: "))

    media = (nota1 + nota2 + nota3) / 3 

    if media >= 70:
        print("Aluno aprovado.")
    elif media >= 60:
        print("Aluno em exame.")
    else:
        print("Aluno reprovado.")

    matricula = int(input("Digite a matrícula do aluno (número negativo para sair): "))

