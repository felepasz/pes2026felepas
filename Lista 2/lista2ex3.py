#3 – Faça um programa que exiba na tela a contagem iniciando no número 1 e indo até um
#número informado pelo usuário. Considere que a contagem pode ser até um número
#positivo ou até um número negativo.
import time 

numero = int(input("Informe um número: "))

if numero > 0:
    for i in range(1, numero + 1):
        print(i)
        time.sleep(0.7)
else:
    for i in range(1, numero - 1, - 1):
        print(i)
        time.sleep(0.7)
