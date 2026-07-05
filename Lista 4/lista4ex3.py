'''3 – Utilizando como base o exercício anterior, faça com seu programa exiba uma saída
formatada da forma exibida abaixo (abaixo é utilizado com exemplo com 3 notas). Você
deve fazer isso de duas formas: com while e com for.
Exibição com while:
Nota: 9.0
Nota: 7.5
Nota: 8.0
Exibição com for:
Nota: 9.0
Nota: 7.5
Nota: 8.0'''

notas = []

notasdig = int(input("digite o numero de notas a serem digitadas: "))

x = 0

while x<notasdig:
    notas.append (float(input("digite a nota: ")))
    x = x + 1

limite = len(notas)
x = 0

print("exibição com While:")
while x<notasdig:
        print(f"nota{x + 1}: {notas[x]}")
        x = x + 1

print("exibição com For:")
for x in range(len(notas)):
    print(f"nota{x + 1}: {notas[x]}")
    x = x + 1