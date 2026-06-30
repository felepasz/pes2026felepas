#2 – Crie um programa que registrará as notas de um estudante. O programa deve
#perguntar ao usuário quantas notas devem ser digitadas e, em seguida, fazer a leitura das
#notas e, ao final, exibir todas as notas digitadas na tela.

notas = []

notasdig = int(input("Digite o numero de notas a serem digitadas: "))

x = 0

while x<notasdig:
    notas.append (input("Digite a nota: "))
    x = x + 1

while x<notasdig:
    print(f"nota{x + 1}: {notas[x]}")
    x = x + 1