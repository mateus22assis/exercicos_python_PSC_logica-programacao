#calculo de multa de transito

velocidadeCarro = float(input("Digite a velocidade do carro em (km/h): "))
valorMulta = 0

agravante = 0

#regras
if velocidadeCarro <= 60:
  infracao = "sem multa"
  
elif velocidadeCarro <= 80:
  infracao = " leve"
  valorMulta = 100
elif velocidadeCarro <= 100:
  infracao = "media "
  valorMulta = 200  
elif velocidadeCarro <= 120:
  infracao = "grave"
  valorMulta = 500

else:
 infracao = "Grave (com agravante)"
 valorMulta = 500 + 200


#saida

print(f"Tipo de multa: {infracao}")
print(f"Valor total: R${valorMulta:.2f}")
