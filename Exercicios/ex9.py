#Implemente um algoritmo que solicite ao usuário a quantidade de salgados consumidos na cantina e o valor do salgado (considere que todos possuem o mesmo preço).Lembre-se que o preço é um número de ponto flutuante e não um inteiro. Em seguida, exiba o valor total da compra.

preco = float(input("o preço dos salgados foi: "))
salgadinhoconsumido = int(input("total de salgadinho consumidos são: "))

divida = preco * salgadinhoconsumido

print("total é:", divida)