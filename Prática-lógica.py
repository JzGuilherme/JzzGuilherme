#usuários cadastrados: 
nome_user = input("Insira o nome de usuário: ")
senha = input("Insira a sua senha: ")
tipo1 = "Acesso total"
tipo2 = "Acesso parcial"
tipo3 = "Acesso restrito"
#admin / 123 / acesso total
#● jose / abc / acesso parcial
#● maria / 456 / acesso restrito
#Saída esperada:
#● Se login correto: “Bem-vindo, [nome]! Seu acesso é: [tipo]”
#● Se incorreto: mensagem de erro
#● Se login correto, mas tentativa de acessar algo não permitido: negar com explicação.
if nome_user == "admin" and senha == "123":
  print(f"Bem-vindo, {nome_user}! Seu tipo de acesso é: {tipo1}")
elif nome_user == "jose" and senha == "abc":
  print(f"Bem-vindo, {nome_user}! Seu tipo de acesso é: {tipo2}")
elif nome_user == "maria" and senha == "456":
  print(f"Bem-vindo, {nome_user}! Seu  tipo de acesso é: {tipo3}, logo será bloqueado por não ser permitido")
else: 
  print("O usuário ou a senha estão incorretos!")
