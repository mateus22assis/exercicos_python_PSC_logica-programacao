'''1. Sistema de Notas com Estatísticas
Crie um programa que:
Receba um vetor com as notas dos alunos. 
Implemente métodos para: 
Calcular a média 
Encontrar a maior nota 
Contar quantos alunos estão acima da média 
Exiba todas essas informações. 
obs: usando metodos
'''


def ler_notas(n):
    notas = [0] * n
    for i in range(n):
        notas[i] = float(input(f"Digite a nota do aluno {i+1}: "))
    return notas


def calcular_media(notas, n):
    soma = 0
    for i in range(n):
        soma += notas[i]
    return soma / n

def encontrar_maior_nota(notas, n):
    maior = notas[0]
    for i in range(1, n):
        if notas[i] > maior:
            maior = notas[i]
    return maior
  
def contar_acima_media(notas, n, media):
    count = 0
    for i in range(n):
        if notas[i] > media:
            count += 1
    return count

# Programa principal
n = int(input("Digite a quantidade de notas a serem inseridas: "))
notas = ler_notas(n)
media = calcular_media(notas, n)
maior_nota = encontrar_maior_nota(notas, n)
acima_da_media = contar_acima_media(notas, n, media)

print(f"A média das notas é: {media}")
print(f"A maior nota é: {maior_nota}")
print(f"Quantidade de alunos acima da média: {acima_da_media}")