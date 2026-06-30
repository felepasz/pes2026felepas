#1 – Implemente um algoritmo com uma lista de nomes de bairros de Garopaba. O nome
#do primeiro bairro deve ser adicionado manualmente (no próprio programa), em seguida,
#deve ser solicitado ao usuário para cadastrar o nome de mais 5 bairros. Ao final, o
#rograma deve exibir o nome de todos os bairros cadastrados na tela.
import time

nome = []
nome.append("Macacu")
x = 1
print("Macacu")

time.sleep(1)

while x<=5:
    nome.append (input("Digite o nome de mais 5 bairros de Garopaba: "))
    x = x + 1

limite = len(nome)

x = 0

print ("Listando...")
while x<limite:
    print (f"Bairro: {nome[x]}")
    x = x+1

    time.sleep(0.5)



