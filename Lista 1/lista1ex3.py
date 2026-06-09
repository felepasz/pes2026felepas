#3 – Construa um algoritmo que solicite o nome de usuário e a senha. Se o nome de
#usuário for igual a "admin" e a senha for igual a "12345", exiba "Login bem-sucedido".
#Caso contrário, exiba "Nome de usuário ou senha incorretos".

usuario = str(input("Solicite o nome: "))
senha = str(input("Digite sua senha: "))

if (senha == "12345" and usuario == "admin"):
    print("Login bem sucedido!")

else :
    print("Nome de usuário ou senha incorretos")