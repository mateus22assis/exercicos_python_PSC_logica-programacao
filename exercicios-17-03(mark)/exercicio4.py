#calculo de situação do empréstimo
#entrada
salario = float(input("Digite o seu salário: "))
valorParcela = float(input("Digite o valor da parcela: "))

#regras
if valorParcela > salario * 0.3:
  situacao = "emprestimo negado"
elif valorParcela <= salario * 0.2:
   situacao = "emprestimo aprovado"
   classificacao = "condição excelente"
else:
    situacao = "emprestimo aprovado"
    classificacao = "condição aceitável"
  

#saida
print(f"Situação do empréstimo: {situacao}")
if situacao == "emprestimo aprovado":
   print(f"Classificação: {classificacao}")