# Cálculo de uma função definida por partes
import math
x = float(input("digite o valor de x: "))

if x < -2:
    resultado = 2 * x + 2

elif x <  3:
    resultado = 3

else:
    resultado = -x

print("O valor de f(x) é:", resultado)