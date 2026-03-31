'''Faça um programa que solicite ao usuário que informe a matrícula e as três notas de um conjunto de alunos. O programa deverá exibir a mensagem informando se o aluno foi aprovado (média maior ou igual a 70), exame (nota maior ou igual a 60 e menor que 70) ou reprovado (nota inferior a 60). O programa irá terminar quando o usuário informar uma matrícula negativa. '''



matricula = int(input("Digite a matrícula do aluno (número negativo para sair): "))


while matricula >= 0: 
   
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    nota3 = float(input("Digite a terceira nota do aluno: "))

    media = (nota1 + nota2 + nota3) 

    if media >= 70:
        print("Aluno aprovado.")
    elif media >= 60:
        print("Aluno em exame.")
    else:
        print("Aluno reprovado.")

    matricula = int(input("Digite a matrícula do aluno (número negativo para sair): "))

