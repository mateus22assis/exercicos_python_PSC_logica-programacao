''' Faça um programa que solicite ao usuário que digite o número do mês do ano, e que imprima o nome do mês correspondente. O programa não poderá utilizar a estrutura condicional IF.'''

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
num_mes = int(input('Digite o numero do mes: '))
print('O mes correspondente é: ', meses[num_mes-1])

