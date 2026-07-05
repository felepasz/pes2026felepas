'''5 – Crie um programa que funcionará como um cadastro de Amigos Próximos no
Instagram. Seu programa deve permitir que amigos sejam cadastrados ou removidos,
conforme a solicitação do usuário. Também deve ser possível exibir a lista com todos os
amigos cadastrados, porém, o programa deve avisar o usuário caso a lista esteja vazia.
Crie um menu, conforme abaixo, para permitir a interação com o seu programa:
Amigos Próximos
---------------
1 - Cadastrar
2 - Excluir
3 - Listar
0 - Sair'''

amigos = []

while True:
    print("\nAmigos Próximos")
    print("---------------")
    print("1 - Cadastrar")
    print("2 - Excluir")
    print("3 - Listar")
    print("0 - Sair")

    opcao = int(input("Opção: "))

    if opcao == 0:
        print("Programa encerrado!")
        break

    elif opcao == 1:
        nome = input("Digite o nome do amigo a ser adicionado: ")
        amigos.append(nome)
        print("Amigo cadastrado com sucesso!")

    elif opcao == 2:
        nome = input("Digite o nome do amigo a ser excluído: ")

        if nome in amigos:
            amigos.remove(nome)
            print("Amigo removido com sucesso!")
        else:
            print("Esse amigo não está na lista.")

    elif opcao == 3:
        if len(amigos) == 0:
            print("A lista de amigos está vazia.")
        else:
            print("Lista de Amigos Próximos:")
            for amigo in amigos:
                print("-", amigo)

    else:
        print("Opção inválida!")
        
        