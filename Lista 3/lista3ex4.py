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

placas = [0] * 15
contplacas = 0
x = 0
i = 0
p = 0
codigoexcluido = 0

while True:
    print ("Menu:")
    print ("----")
    print ("1 – Cadastrar")
    print ("2 – Excluir")
    print ("3 - Listar")
    print ("0 – Sair ")

    opcao = int(input("selecione uma opção: "))

    if opcao == 0:
        break
    elif opcao == 1:
        if contplacas <= 14:
            