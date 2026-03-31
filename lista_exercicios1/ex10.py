numeroEleitores = int(input("Digite o número de eleitores: "))
numeroVotosCandidatoA = int(input("Digite o número de votos do candidato A: "))
numeroVotosCandidatoB = int(input("Digite o número de votos do candidato B: "))

percentualVotosCandidatoA = (numeroVotosCandidatoA / numeroEleitores) * 100
print(f"O percentual de votos do candidato A é: {percentualVotosCandidatoA:.2f}%")
percentualVotosCandidatoB = (numeroVotosCandidatoB / numeroEleitores) * 100
print(f"O percentual de votos do candidato B é: {percentualVotosCandidatoB:.2f}%")
percentualVotosNulos = 100 - (percentualVotosCandidatoA + percentualVotosCandidatoB)
print(f"O percentual de votos nulos é: {percentualVotosNulos:.2f}%")
