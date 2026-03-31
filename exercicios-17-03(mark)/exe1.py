notaFinal = float(input("Digite a nota final (0-10): "))
frequencia = float(input("Digite a frequência (0-100): "))


if frequencia < 75 :
  situacao = "reprovado por falta"
else:
  if notaFinal >= 7:
    situacao = "aprovado"
  elif notaFinal >=5:
    situacao = "recuperação"
  else:
    situacao = "reprovado por nota"
print(f"situaçao final do aluno: {situacao}")