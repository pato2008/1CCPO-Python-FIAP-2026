# logica e (and)

verifica_email = True
verifica_senha = False

login = verifica_email and verifica_senha
print(login)

if login:
    print(" entra no sistema")


if not login : print("erro otario")