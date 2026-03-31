import math
x = float(input("Digite um número:"))
quadrado = math.pow(x, 2)
cubo = math.pow(x, 3)
raiz_quadrada = math.sqrt(x)
raiz_cubica = math.pow(x, 1/3)

print(f"O número digitado ao quadrado: {quadrado}")
print(f"O número digitado ao cubo: {cubo}")
print(f"A raiz quadrada do número digitado: {raiz_quadrada:.2f}")
print(f"A raiz cúbica do número digitado: {raiz_cubica:.2f}")