#4 - Codifique um programa que funcionará como um cadastro de placas de automóveis de
#um estacionamento (para até 15 automóveis). O cadastro deve ser realizado em uma
#lista. Seu programa deve ter um menu com a seguinte estrutura:
#1 – Cadastrar
#2 - Excluir
#3 - Listar
#0 - Sair
#A opção Cadastrar deve verificar se há espaço disponível na lista para o cadastro. Se
#houver, deve proceder o cadastro. Se não, deve informar o usuário que não há espaço
#disponível. A opção Excluir deve perguntar ao usuário qual placa deve ser excluída (pelo
#nome da placa) e informar se houve sucesso ou falha. Já a opção listar deve
#simplesmente listar todas as placas cadastradas. Dica: utilize um valor padrão para definir
#um espaço vago na lista.

placas = ["VAGO"] * 15

while True:
    print("\n1 - Cadastrar")
    print("2 - Excluir")
    print("3 - Listar")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        placa = input("Digite a placa: ")

        encontrou_vaga = False

        for i in range(15):
            if placas[i] == "VAGO":
                placas[i] = placa
                encontrou_vaga = True
                print("Placa cadastrada com sucesso!")
                break

        if encontrou_vaga == False:
            print("Não há espaço disponível.")

    elif opcao == "2":
        placa = input("Digite a placa a excluir: ")

        encontrou = False

        for i in range(15):
            if placas[i] == placa:
                placas[i] = "VAGO"
                encontrou = True
                print("Placa excluída com sucesso!")
                break

        if encontrou == False:
            print("Falha: placa não encontrada.")

    elif opcao == "3":
        print("\nPlacas cadastradas:")

        vazio = True

        for i in range(15):
            if placas[i] != "VAGO":
                print(placas[i])
                vazio = False

        if vazio == True:
            print("Nenhuma placa cadastrada.")

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")