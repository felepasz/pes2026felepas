'''2 - A situação de logística da Empresa Alpha Entregas está necessitando de melhorias no
controle das saídas e retornos dos caminhões:
a) Considere que a empresa possui 8 caminhões numerados de 001 a 008;
b) Cada caminhão tem seu respectivo condutor, a relação dos condutores e seus
códigos está abaixo;
c) As entregas são monitoradas através do controle no retorno de cada caminhão;
d) Precisamos receber os dados do código do caminhão e do código do condutor,
somente assim consideraremos que a mercadoria daquela rota foi entregue;
e) O algoritmo deve prever o cadastro dos caminhões e dos condutores;
f) O algoritmo deve prever um cadastro com uma lista de todos os caminhões que
saem diariamente;
g) A cada saída diária dos caminhões, deve-se registrar a data e hora de saída de
cada veículo, bem como o condutor responsável;
h) Quando do retorno de cada caminhão, deve-se registrar a data e hora de
chegada;
i) O sistema deve ter opções para verificar se um determinado caminhão retornou da
rota ou não, mostrando a data, hora e nome do condutor, consultando por código do
veículo;
j) O sistema deve ter opções para listar o cadastro de caminhões;
k) O sistema deve ter opções para listar os condutores;
l) O sistema deve ter opções para listar, por data, a lista dos veículos que
retornaram;
m) Precisamos saber, em determinado momento, se todas as entregas do dia foram
realizadas.
Relação de Condutores:
001 – Roberto Souza
002 – João Graciano
003 – Karine Silva
004 – Pedro Luiz
005 – Maria Catarina
006 – Júlio Cardoso
007 – Altivo Antônio
008 – Jorge Gonçalves
009 – Marcos Vinícius
010 – Heleno Nunes
011 – Mara Cristina
012 – Otávio Rocha
Relação dos Veículos
001 – Monobloco
002 – Scania 112 HW
003 – Volkswagen Express 4150
004 – Volkswagen Express 6160
005 – Volkswagen VW 17230 Worker
006 – Volkswagen Express 9170
007 – Iveco Daily 40s14
008 – Iveco Tectro 310E28'''

condutores = {
    "001": "Roberto Souza",
    "002": "João Graciano",
    "003": "Karine Silva",
    "004": "Pedro Luiz",
    "005": "Maria Catarina",
    "006": "Júlio Cardoso",
    "007": "Altivo Antônio",
    "008": "Jorge Gonçalves",
    "009": "Marcos Vinícius",
    "010": "Heleno Nunes",
    "011": "Mara Cristina",
    "012": "Otávio Rocha"
}

veiculos = {
    "001": "Monobloco",
    "002": "Scania 112 HW",
    "003": "Volkswagen Express 4150",
    "004": "Volkswagen Express 6160",
    "005": "Volkswagen VW 17230 Worker",
    "006": "Volkswagen Express 9170",
    "007": "Iveco Daily 40s14",
    "008": "Iveco Tectro 310E28"
}

rotas = []

while True:
    print("\n========== ALPHA ENTREGAS ==========")
    print("1 - Listar caminhoes")
    print("2 - Listar condutores")
    print("3 - Registrar saida")
    print("4 - Registrar retorno")
    print("5 - Consultar caminhao")
    print("6 - Listar retornos por data")
    print("7 - Verificar entregas do dia")
    print("0 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        print("\n--- CAMINHOES ---")

        for codigo in veiculos:
            print(codigo, "-", veiculos[codigo])

    elif opcao == "2":
        print("\n--- CONDUTORES ---")

        for codigo in condutores:
            print(codigo, "-", condutores[codigo])

    elif opcao == "3":
        print("\n--- CAMINHOES ---")

        for codigo in veiculos:
            print(codigo, "-", veiculos[codigo])

        codigo_veiculo = input("Digite o codigo do caminhao: ")

        if codigo_veiculo in veiculos:
            print("\n--- CONDUTORES ---")

            for codigo in condutores:
                print(codigo, "-", condutores[codigo])

            codigo_condutor = input("Digite o codigo do condutor: ")

            if codigo_condutor in condutores:
                # O usuario informa a data e a hora da saida
                data_saida = input("Digite a data de saida (DD/MM/AAAA): ")
                hora_saida = input("Digite a hora de saida (HH:MM): ")

                rota = {
                    "veiculo": codigo_veiculo,
                    "condutor": codigo_condutor,
                    "data_saida": data_saida,
                    "hora_saida": hora_saida,
                    "data_retorno": "",
                    "hora_retorno": ""
                }

                rotas.append(rota)

                print("Saida registrada.")
            else:
                print("Condutor nao cadastrado.")
        else:
            print("Caminhao nao cadastrado.")

    elif opcao == "4":
        codigo_veiculo = input("Digite o codigo do caminhao: ")

        if codigo_veiculo in veiculos:
            encontrou = False

            indice = len(rotas) - 1

            while indice >= 0:
                if rotas[indice]["veiculo"] == codigo_veiculo:
                    if rotas[indice]["data_retorno"] == "":
                        # O usuario informa a data e a hora do retorno
                        data_retorno = input("Digite a data de retorno (DD/MM/AAAA): ")
                        hora_retorno = input("Digite a hora de retorno (HH:MM): ")

                        rotas[indice]["data_retorno"] = data_retorno
                        rotas[indice]["hora_retorno"] = hora_retorno

                        print("Retorno registrado.")

                        encontrou = True
                        break

                indice = indice - 1

            if encontrou == False:
                print("Nao existe uma saida pendente para esse caminhao.")
        else:
            print("Caminhao nao cadastrado.")

    elif opcao == "5":
        codigo_veiculo = input("Digite o codigo do caminhao: ")

        if codigo_veiculo in veiculos:
            encontrou = False
            indice = len(rotas) - 1

            while indice >= 0:
                if rotas[indice]["veiculo"] == codigo_veiculo:
                    print("\n--- CONSULTA ---")
                    print("Caminhao:", veiculos[codigo_veiculo])
                    print("Condutor:", condutores[rotas[indice]["condutor"]])
                    print("Data de saida:", rotas[indice]["data_saida"])
                    print("Hora de saida:", rotas[indice]["hora_saida"])

                    if rotas[indice]["data_retorno"] == "":
                        print("Situacao: AINDA NAO RETORNOU")
                    else:
                        print("Situacao: RETORNOU")
                        print("Data de retorno:", rotas[indice]["data_retorno"])
                        print("Hora de retorno:", rotas[indice]["hora_retorno"])

                    encontrou = True
                    break

                indice = indice - 1

            if encontrou == False:
                print("Esse caminhao ainda nao possui saida registrada.")
        else:
            print("Caminhao nao cadastrado.")

    elif opcao == "6":
        data = input("Digite a data no formato DD/MM/AAAA: ")
        encontrou = False

        print("\n--- CAMINHOES QUE RETORNARAM ---")

        for rota in rotas:
            if rota["data_retorno"] == data:
                print(
                    rota["veiculo"],
                    "-",
                    veiculos[rota["veiculo"]],
                    "-",
                    condutores[rota["condutor"]],
                    "-",
                    rota["hora_retorno"]
                )
                encontrou = True

        if encontrou == False:
            print("Nenhum caminhao retornou nessa data.")

    elif opcao == "7":
        data = input("Digite a data no formato DD/MM/AAAA: ")

        total_saidas = 0
        total_retornos = 0

        for rota in rotas:
            if rota["data_saida"] == data:
                total_saidas = total_saidas + 1

                if rota["data_retorno"] != "":
                    total_retornos = total_retornos + 1

        print("\n--- SITUACAO DAS ENTREGAS ---")
        print("Saidas:", total_saidas)
        print("Retornos:", total_retornos)

        if total_saidas == 0:
            print("Nao existem saidas nessa data.")
        elif total_saidas == total_retornos:
            print("TODAS AS ENTREGAS DO DIA FORAM REALIZADAS.")
        else:
            print("AINDA EXISTEM ENTREGAS PENDENTES.")

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opcao invalida.")
