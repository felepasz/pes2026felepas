'''1 – Crie um programa com uma função para calcular a média aritmética simples entre 3
notas. Seu programa deve solicitar 3 notas, chamar a função e exibir o resultado na tela.'''

def mediaari( a, b, c):
    m = (a + b + c)/3
    return m

num1 = int(input("Digite primeiro numero: "))
num2 = int(input("Digite segundo numero: "))
num3 = int(input("Digite terceiro numero: "))

r = mediaari( num1, num2, num3)

print(" Resultado: ", r)