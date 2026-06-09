#Implemente um algoritmo que leia a quantidade de partidas de um campeonato de futebol e indique a quantidade de minutos total (de todas as partidas juntas).Considere que cada partida terá sempre o mesmo tempo.Comente seu algoritmo.

totalminperpart = int(input("total de minutos por partida é: "))
quantpart = int(input("total de partidas no campeonato: "))

minutosjogado = totalminperpart*quantpart

print("o total de minutos jogados no campeonato é de: ", minutosjogado, "minutos")