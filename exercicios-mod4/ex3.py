# Cálculo das raízes de uma equação quadrática
import math


a = float(input("Digite o coeficiente 'a': "))
b = float(input("Digite o coeficiente 'b': "))
c = float(input("Digite o coeficiente 'c': "))

delta = b**2 - 4*a*c

print(f"Delta calculado: {delta}")



if delta < 0:
    print("Não existe raiz real.")


elif delta == 0:
    x = (-b) / (2 * a)
    print(f"Existe somente uma raiz real: x = {x}")


else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"Existem duas raízes reais: x1 = {x1} e x2 = {x2}")