#programa de gerenciamento das notas de uma turma, onde o usuário digita a matrícula do aluno e suas três notas. O programa deve calcular a média do aluno e apresentar se ele foi aprovado (média maior ou igual a 70), em exame (média entre 60 e 69) ou reprovado (média menor que 60). O programa deve continuar solicitando a matrícula e as notas dos alunos até que o usuário digite um número negativo para a matrícula.
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

