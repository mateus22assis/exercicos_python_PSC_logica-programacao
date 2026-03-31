contador = 0
for i in range(10):
  numero =  int(input("Digite um numero: "))
  if numero < 0:
    contador += 1

print("foram lidos", contador, "numeros negativos")
 