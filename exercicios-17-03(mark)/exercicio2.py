
#entrada
valorCompra = float(input("Digite o valor da compra: "))
cupom = input("Digite o cupom de desconto: ").upper()

#aplicaçao das regras
if cupom == "DESC10":
  valorDesconto = valorCompra * 0.10
elif cupom == "DESC20":
  valorDesconto = valorCompra * 0.20
else:
  valorDesconto = 0

if valorCompra >= 200:
  valorFrete = 0
else:
  valorFrete = 15

valorFinal = valorCompra - valorDesconto + valorFrete

#saida
print(f"Valor do desconto: R${valorDesconto:.2f}")
print(f"Frete: R${valorFrete:.2f}")
print(f"Valor final: R${valorFinal:.2f}")