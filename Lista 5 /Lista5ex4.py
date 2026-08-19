'''4 – Desenvolva um algoritmo com uma função que receba uma lista numérica e retorne o
resultado da soma de todos os elementos dela. Seu programa principal deve solicitar 4
números ao usuário, chamar a função e exibir o resultado da soma na tela.'''

def somar_lista(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma

numeros = []

for i in range(4):
    numero = float(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

resultado = somar_lista(numeros)

print(f"A soma dos números é: {resultado}")