'''6. Faça um programa que solicite ao usuário que informe inicialmente os 6 números sorteados na Mega Sena. Em seguida, peça que ele digite os 6 números do cartão que jogou. Imprima a quantidade de pontos que ele fez no concurso.S'''

tamnho_vetor = 6
sorteio = [0] * tamnho_vetor

for i in range(tamnho_vetor):
    sorteio[i] = int(input(f"Digite o número sorteado {i+1}: "))

cartao = [0] * tamnho_vetor

for i in range(tamnho_vetor):
    cartao[i] = int(input(f"Digite o número do cartão {i+1}: "))

pontos = 0 

for i in range(tamnho_vetor):
    if cartao[i] in sorteio:
        pontos += 1
      

print(f"Você fez {pontos} pontos no concurso.")


