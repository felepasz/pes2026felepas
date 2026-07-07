'''7 – Utilizando como base o exercício 6, implemente dois novos recursos: um para
informar a maior nota cadastrada e outro para informar a menor nota cadastrada. Caso
não existam notas cadastradas, seu programa deve informar “Erro: não há notas
cadastradas”. Crie um menu, conforme abaixo, para permitir a interação com o seu
programa:
Notas
-----
1 - Cadastrar
2 - Excluir
3 - Listar
4 - Calcular média
5 – Mostrar maior nota
6 – Mostrar menor nota
0 - Sair
Opção:'''

notas = []

while True:
    print("\nNotas")
    print("-----")
    print("1 - Cadastrar")
    print("2 - Excluir")
    print("3 - Listar")
    print("4 - Calcular média")
    print("5 - Mostrar maior nota")
    print("6 - Mostrar menor nota")
    print("0 - Sair")

    opcao = int(input("Opção: "))

    if opcao == 0:
        print("Programa encerrado!")
        break

    elif opcao == 1:
        nota = float(input("Digite a nota: "))
        notas.append(nota)
        print("Nota cadastrada!")

    elif opcao == 2:
        if len(notas) == 0:
            print("Erro: não há notas cadastradas")
        else:
            indice = int(input("Digite o índice da nota a ser removida: "))

            if indice >= 0 and indice < len(notas):
                notas.pop(indice)
                print("Nota removida!")
            else:
                print("Índice inválido!")

    elif opcao == 3:
        if len(notas) == 0:
            print("Erro: não há notas cadastradas")
        else:
            for i in range(len(notas)):
                print(i, "-", notas[i])

    elif opcao == 4:
        if len(notas) == 0:
            print("Erro: não há notas cadastradas")
        else:
            media = sum(notas) / len(notas)
            print("Média:", media)

            if media >= 6:
                print("Situação: Aprovado")
            else:
                print("Situação: Reprovado")

    elif opcao == 5:
        if len(notas) == 0:
            print("Erro: não há notas cadastradas")
        else:
            print("Maior nota:", sorted(notas, reverse=True))

    elif opcao == 6:
        if len(notas) == 0:
            print("Erro: não há notas cadastradas")
        else:
            print("Menor nota:", sorted(notas))

    else:
        print("Opção inválida!")