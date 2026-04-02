# Calculo do percentual de votos de um candidato, onde o usuário digita o número de eleitores, o número de votos do candidato A e o número de votos do candidato B. O programa deve calcular e apresentar o percentual de votos de cada candidato e o percentual de votos nulos.
numeroEleitores = int(input("Digite o número de eleitores: "))
numeroVotosCandidatoA = int(input("Digite o número de votos do candidato A: "))
numeroVotosCandidatoB = int(input("Digite o número de votos do candidato B: "))

percentualVotosCandidatoA = (numeroVotosCandidatoA / numeroEleitores) * 100
print(f"O percentual de votos do candidato A é: {percentualVotosCandidatoA:.2f}%")
percentualVotosCandidatoB = (numeroVotosCandidatoB / numeroEleitores) * 100
print(f"O percentual de votos do candidato B é: {percentualVotosCandidatoB:.2f}%")
percentualVotosNulos = 100 - (percentualVotosCandidatoA + percentualVotosCandidatoB)
print(f"O percentual de votos nulos é: {percentualVotosNulos:.2f}%")
