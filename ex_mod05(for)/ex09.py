#programa que recebe um número do usuário e imprime todos os números ímpares de 1 até esse número usando um loop 
numero = int(input("Digite um número: "))
for  i in range(1, numero + 1):
  if i % 2 != 0:
    print(i)