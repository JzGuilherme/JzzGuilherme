nome = input("Qual é seu nome? ")
n1 = float(input("Qual é a sua primeira nota? "))
n2 = float(input("Qual é a sua segunda nota? "))
qtdf = int(input("Quantidade de faltas: "))
média = (n1*n2)/2
if média < 5:
  print("Reprovado")
elif 5 <= média < 7:
  print("Recuperação")
elif média >= 7:
  print("Aprovado")
elif qtdf == 15:
  print("Reprovado por falta, independentemente da nota")
else:
  print("Aprovado")
