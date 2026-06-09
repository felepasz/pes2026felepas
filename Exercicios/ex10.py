#Implemente um algoritmo que solicite ao usuário a quantidade de salgados consumidos na cantina e o valor do salgado (considere que todos possuem o mesmo preço). Solicite também ao usuário a quantidade de sucos consumida e o valor do suco (considere, também, que todos possuem o mesmo preço). Em seguida, exiba o valor total da compra.

precosalgado = float(input("o preço dos salgados é: "))
salgadinhoconsumido = int(input("total de salgadinho consumidos são: "))
precosuco = float(input("o preço do suco é: "))
sucoconsumido = int(input("o total de sucos consumidos são: "))

divida = (precosalgado * salgadinhoconsumido)+(precosuco * sucoconsumido)

print("total é:", divida,"R$")