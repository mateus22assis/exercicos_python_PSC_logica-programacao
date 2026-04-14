'''. Faça um programa que leia um vetor com 10 elementos inteiros. Solicite ao usuário que informe um novo número, e verifique se este número encontra-se no vetor. Caso positivo, imprima a(s) posição(ões) em que este número estiver no vetor. Caso contrário, exiba uma mensagem avisando ao usuário informando que o número não se encontra no vetor.'''

tamanho_vetor = 10
vetor = [0] * tamanho_vetor 

for i in range(tamanho_vetor):
    vetor[i] = int(input(f"Digite o elemento {i+1}: "))

numero = int(input("Digite um número: "))

encontrado = False
for i in range(tamanho_vetor):
    if vetor[i] == numero:
        print(f"O número {numero} está na posição {i+1}")
        encontrado = True

if not encontrado:
    print(f"O número {numero} não se encontra no vetor.")
