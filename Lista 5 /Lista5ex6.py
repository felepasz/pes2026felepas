'''6 - Crie uma função chamada tempo_total que receba a quantidade de horas e minutos
que um jovem passou jogando videogame e retorne o total de minutos jogados. Peça ao
usuário para inserir as horas e minutos, e exiba o tempo total em minutos.'''

def tempo_total(horas, minutos):
    total = horas * 60 + minutos
    return total


horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))

resultado = tempo_total(horas, minutos)

print("Tempo total jogado:", resultado, "minutos")


