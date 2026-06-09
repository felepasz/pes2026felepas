#10 - Escreva um programa que leia números inteiros do teclado. O programa deve ler os
#números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de
#números digitados, assim como a soma e a média aritmética.

i = 0
somanum = 0
num = 1

while num!=0:
    num = int(input("Digite um numero: "))
    if num != 0:
     somanum = num + somanum
     i = i + 1 
media = somanum/i

print(f"o total de numeros digitados foi {i}, a soma deles foi {somanum}, e a aritimetica deles doi {media}")