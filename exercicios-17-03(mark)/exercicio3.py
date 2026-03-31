"""Calcule o IMC e classifique:
Fórmula:
IMC = peso / (altura * altura)
Classificação:
< 18.5 → Abaixo do peso
18.5 a 24.9 → Peso normal
25 a 29.9 → Sobrepeso
≥ 30 → Obesidade
Mensagem adicional:
Se IMC ≥ 30 → “Procure orientação médica”
Entrada:
Peso (kg)
Altura (m)
Saída:
IMC
Classificação
Mensagem extra (se necessário)
"""
#entrada
Peso = float(input("Digite o seu peso em (kg): "))
Altura = float(input("Digite a sua altura em (m): "))

#calculo
IMC = Peso / (Altura ** 2)

#aplicaçao das regras
if  IMC < 18.5:
  classificacao = "abaixo do peso"
elif IMC <= 24.9:
  classificacao = "peso normal"
elif IMC <= 29.9:
  classificacao = "sobrepeso" 
else:
  classificacao = "obesidade"


#saida
print(f"Seu IMC é: {IMC:.2f}")
print(f"Classificação: {classificacao}")

if classificacao == "obesidade":
  print("aviso: procure orientação médica")