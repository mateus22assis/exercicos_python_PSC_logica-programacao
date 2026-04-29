'''4. Análise de Frequência de Números (mais avançado)
Crie um programa que:
Receba um vetor de números inteiros 
Crie métodos para: 
Contar quantas vezes cada número aparece 
Inverter o vetor
'''

def ler_numeros(n):
    numeros = [0] * n
    for i in range(n):
        numeros[i] = int(input(f"Digite o número {i+1}: "))
    return numeros

def contar_frequencia(numeros, n):
    frequencia = [0] * n 
    for i in range(n):
        count = 0
        for j in range(n): 
            if numeros[i] == numeros[j]:
                count += 1
        frequencia[i] = count
    return frequencia

def inverter_vetor(numeros, n):
    numeros_invertidos = [0] * n
    for i in range(n):
        numeros_invertidos[(n - 1 - i)] = numeros[i]
    return numeros_invertidos

# Programa principal
n = int(input("Digite a quantidade de números a serem inseridos: "))
numeros = ler_numeros(n)
frequencia = contar_frequencia(numeros, n)
numeros_invertidos = inverter_vetor(numeros, n)


for i in range(n):
    print(f"O número {numeros[i]} aparece {frequencia[i]} vezes.")


print("Vetor invertido:")
print(numeros_invertidos)
