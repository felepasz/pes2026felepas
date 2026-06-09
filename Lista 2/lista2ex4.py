#4 – Implemente um algoritmo que exiba na tela os números pares de 0 até um número
#digitado pelo usuário. Dica: você pode utilizar o operador módulo (%) ou contar de 2 em 2.

numero = int(input("Informe um número: "))

for i in range(0, numero + 1):
    if i % 2 == 0:
        print(i)