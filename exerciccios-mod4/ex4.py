
peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (m): "))

imc = peso / (altura ** 2)

print(f"\nSeu IMC é: {imc:.2f}")


if imc < 20:
    situacao = "Abaixo do peso"
    
elif imc < 25:     situacao = "Peso Normal"
    
elif imc < 30: 
    situacao = "Sobre Peso"
    
elif imc < 40: 
    situacao = "Obeso"
    
else: 
    situacao = "Obeso Mórbido"

print(f"Situação: {situacao}")