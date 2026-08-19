'''6 - Crie uma função chamada tempo_total que receba a quantidade de horas e minutos
que um jovem passou jogando videogame e retorne o total de minutos jogados. Peça ao
usuário para inserir as horas e minutos, e exiba o tempo total em minutos.'''

def tempo_total(h, m):
    i = h*60
    r = i + m 
    return r

horas = int(input("Digite o numero de horas que você jogou: "))
minutos = int(input("Digite a quantidade de minutos também: "))


