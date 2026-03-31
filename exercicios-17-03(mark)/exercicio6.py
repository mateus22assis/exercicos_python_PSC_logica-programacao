# --- ENTRADA ---
valorCompra = float(input("Digite o valor da compra: R$ "))
valorPago = float(input("Digite o valor pago: R$ "))

#  REGRAS 
situacao = ""
troco = 0

if valorPago < valorCompra:
    situacao = "Valor insuficiente"
elif valorPago == valorCompra:
    situacao = "Pagamento exato"
else:
    situacao = "Pagamento aprovado"
    troco = valorPago - valorCompra

#  SAIDA 
print(f"Situação: {situacao}")

if troco > 0:
    print(f"Troco: R${troco:.2f}")

if troco > 100:
    print("Troco alto, conferir notas")