'''Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma cidade , em um determinado dia. Para cada casa consultada, foi fornecido o numero do canal  (4,5,7,12) e o numero de pessoas que estavam assistindo àquele canal. Faça um programa que : 
a ) Leia um número indeterminado de dados (Numero de canal e numero de pessoas assistindo ); 
b) Calcule e mostre o percentual de audiência de cada canal.
Para encerrar a entrada de dados, digite o número do canal ZERO . 
'''
numero_canal = int(input("Digite o número do canal (4,5,7,12: "))

while numero_canal in [4, 5, 7, 12]:
    numero_pessoas = int(input("Digite o número de pessoas assistindo: "))
    
    # Aqui você pode armazenar os dados para calcular os percentuais posteriormente
    
    numero_canal = int(input("Digite o número do canal (4,5,7,12: "))

# Após a entrada de dados, você pode calcular e mostrar os percentuais de audiência para cada canal
for canal in [4, 5, 7, 12]:
    # Calcule o percentual de audiência para o canal e mostre o resultado
    pass  # Substitua por sua lógica de cálculo e exibição dos resultados