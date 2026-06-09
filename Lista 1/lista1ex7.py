#7 - Qual é o seu Signo? Solicite o dia e o mês de nascimento do usuário. Com base
#nesses valores, use condicionais para determinar o signo.

dia = int(input("Digite o dia do seu nascimento: "))
mes = int(input("Digite o mês do nascimento: "))

if (mes == 3 and dia >= 21) or (mes == 4 and dia<=19):
    print("Você é de áries")

if (mes == 4 and dia >= 20) or (mes == 5 and dia<=20):
    print("Você é de touro")

if (mes == 5 and dia >= 21) or (mes == 6 and dia<=20):
    print("Você é de gemeos")

if (mes == 6 and dia >= 21) or (mes == 7 and dia<=22):
    print("Você é de cancer")

if (mes == 7 and dia >= 23) or (mes == 8 and dia<=22):
    print("Você é de leao")

if (mes == 8 and dia >= 23) or (mes == 9 and dia<=22):
    print("Você é de virgem")

if (mes == 9 and dia >= 23) or (mes == 10 and dia<=22):
    print("Você é de libra")

if (mes == 10 and dia >= 23) or (mes == 11 and dia<=21):
    print("Você é de escorpião")

if (mes == 11 and dia >= 22) or (mes == 12 and dia<=21):
    print("Você é de sargitario")

if (mes == 12 and dia >= 22) or (mes == 1 and dia<=19):
    print("Você é de capricornio")

if (mes == 1 and dia >= 20) or (mes == 2 and dia<=18):
    print("Você é de aquario")

if (mes == 2 and dia >= 19) or (mes == 3 and dia<=20):
    print("Você é de peixes")

