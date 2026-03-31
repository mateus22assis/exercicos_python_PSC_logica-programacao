qtde_alunos_nota90 = 0
qtde_alunos_reprovados = 0
maior_nota = -1 
menor_nota = 101 
soma_notas = 0
qtde_alunos = 0


notaFinal = float(input("Digite a nota final do aluno (número negativo para sair): "))

while notaFinal >= 0: 
    faltsTotal = int(input("Digite o total de faltas do aluno: "))

    if notaFinal >= 90:
        qtde_alunos_nota90 += 1
    if notaFinal < 70 or faltsTotal >= 20:
        qtde_alunos_reprovados += 1
    
   
    if notaFinal > maior_nota:
        maior_nota = notaFinal
    if notaFinal < menor_nota:
        menor_nota = notaFinal
    
    soma_notas += notaFinal
    qtde_alunos += 1

    
    notaFinal = float(input("Digite a nota final do aluno (número negativo para sair): "))


if qtde_alunos > 0:
    media_notas = soma_notas / qtde_alunos
else:
    media_notas = 0 

print("Quantidade de alunos com nota final maior ou igual a 90: ", qtde_alunos_nota90)
print("Quantidade de alunos reprovados por nota ou por falta: ", qtde_alunos_reprovados)
print("Maior nota: ", maior_nota)
print("Menor nota: ", menor_nota)
print("Média de notas da turma: ", media_notas)