'''6. Faça um programa que solicite ao usuário que informe inicialmente os 6 números sorteados na Mega Sena. Em seguida, peça que ele digite os 6 números do cartão que jogou. Imprima a quantidade de pontos que ele fez no concurso.S'''
tamnho_vetor = 6
resultado = [0] * tamnho_vetor
jogo = [0] * tamnho_vetor
contador = 0


print ("informe seu jogo: ")
for i in range(tamnho_vetor):
    jogo[i] = int(input(f"Digite o número sorteado : "))

print ("informe os números sorteados: ")
for i in range(tamnho_vetor):
    resultado[i] = int(input(f"Digite o número sorteado: "))

for i in range(tamnho_vetor):
    for j in range(tamnho_vetor):
        if jogo[i] == resultado[j]:
            contador += 1
            

print(f"Você fez {contador} pontos no concurso.")

