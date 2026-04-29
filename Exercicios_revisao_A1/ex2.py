'''2. Manipulação de Vetores (Menu Interativo)
Crie um menu com opções:
Inserir valores no vetor 
Remover um valor específico 
Buscar um valor (retornar posição) 
Exibir o vetor
usando métodos 
'''
#def inserir_valores(n):
def inserir_valores(valores, n):
  valores = [0] * n
  for i in range(n):
    valores[i] = int(input(f"Digite o valor para a posição {i}: "))
  return valores

#def exibir_vetor(v, n):
def exibir_vetor(valores, n):
    print("Vetor:", end=" ")
    for i in range(n):
        print(valores[i], end=" ")
    print()

#def buscar_valor(valores, n, valor):
def buscar_valor(valores,n, valor):
  for i in range(n):
     if valores[i] == valor:
        return i
  return -1
    
#def remover_valor(valores, n, valor):
def remover_valor(valores, n, valor):
   for i in range(n):
      if valores[i] == valor:
         valores[i] = -1
         return True
   return False
    # Substitui o valor encontrado por 0 (ou outro valor que indique remoção)



# Programa principal

n = int(input("Digite a quantidade de valores a serem inseridos: "))
vetor = inserir_valores(n)

print('vetor inicial:')
exibir_vetor(vetor, n)      

valor = int(input("Digite o valor a ser buscado: "))
posicao = buscar_valor(vetor, n, valor)

if posicao != -1:
    print(f"Valor encontrado na posição: {posicao}")
else:
    print("Valor não encontrado no vetor.")

valor = int(input("Digite o valor a ser removido: "))
removido = remover_valor(vetor, n, valor)
if removido:
   print(f"Valor {valor} removido do vetor.")
else:   print(f"Valor {valor} não encontrado no vetor.")

print('vetor final:')
exibir_vetor(vetor, n)




   
