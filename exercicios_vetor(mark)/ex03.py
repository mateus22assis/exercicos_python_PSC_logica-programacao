'''. Faça um programa que leia um vetor com 10 elementos inteiros. Solicite ao usuário que informe um novo número, e verifique se este número encontra-se no vetor. Caso positivo, imprima a(s) posição(ões) em que este número estiver no vetor. Caso contrário, exiba uma mensagem avisando ao usuário informando que o número não se encontra no vetor.'''

tamanho_vetor = 10

vetor = [int(input(f"Digite o {i+1}º número do vetor: ")) for i in range(tamanho_vetor)]

numero = int(input("Digite um número para verificar se ele está no vetor: "))

if numero in vetor:
    print(f"O número {numero} está no vetor nas posições:")
    for i, num in enumerate(vetor):
        if num == numero:
            print(f"Posição {i}")
else:
    print(f"O número {numero} não está no vetor.")  