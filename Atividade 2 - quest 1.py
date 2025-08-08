nome = input("Digite seu nome: ")
perfil = input("Digite seu perfil de acesso: ")
dia = input("Qual o dia da Semana? ")
horas = int(input("Digite o horário: "))
if perfil == "adm":
  print("Acesso liberado")
elif perfil == "fin" and horas >= 8 or horas <= 18:
  print("Acesso liberado")
elif perfil == "tecnico":
    if dia == "domingo":
      print("Acesso negado")
    elif horas >= 6 or horas <= 22:
      print("Acesso liberado")
    else:
      print("Acesso negado")
else:
  print("Acesso negado")
