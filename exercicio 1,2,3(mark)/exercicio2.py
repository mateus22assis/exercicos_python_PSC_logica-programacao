#Faça um programa que receba o ano de nascimento de uma pessoa, o ano atual e imprima:
#A idade da pessoa no ano atual
#A idade que a pessoa terá em 2050
print("Calculadora de idade")   

ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))  
idade = ano_atual - ano_nascimento
idade_2050 = 2050 - ano_nascimento

print("A idade da pessoa no ano atual é: ", idade)
print("A idade que a pessoa terá em 2050 é: ", idade_2050)