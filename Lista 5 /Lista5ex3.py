'''3 – Codifique um programa com uma função para calcular o volume de um cilindro. Seu
programa principal deve solicitar a altura e o raio do cilindro em metros, chamar a função
e exibir o resultado na tela. '''
import math

def calcular_volume(altura, raio):
    return math.pi * raio**2 * altura

altura = float(input("Digite a altura do cilindro (em metros): "))
raio = float(input("Digite o raio do cilindro (em metros): "))

volume = calcular_volume(altura, raio)

print("o volume do cilindro é: ", volume)