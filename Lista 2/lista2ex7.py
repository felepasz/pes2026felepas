#7 – Implemente um programa para calcular sua média final em uma determinada unidade
#curricular. O programa deve solicitar ao usuário a quantidade de notas, o valor para cada
#uma das notas e exibir, ao final, a média aritmética simples e informar se o(a) estudante
#está Aprovado ou Reprovado. Considere que a média mínima para a aprovação é 6.

quantnotas = int(input("Insira a quantidade de notas que existem: "))

i = 1
notatotal = 0

while i<= quantnotas:
    msg = f"insira a {i} nota: "
    num = float(input(msg))
    notatotal = notatotal + num
    i = i + 1

notafinal = notatotal/quantnotas

print("sua media foi: ", notafinal)

if notafinal>=6:
    print("voce foi aprovado!")
else:
    print("voce foi reprovado!")
