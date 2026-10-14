'''9 – Utilizando a biblioteca pickle, implemente duas novas opções para salvar e carregar
dados do disco, utilizando como base, o exercício 7.'''

import pickle

class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def exibir(self):
        return f"{self.nome}, {self.idade} anos, {self.altura:.2f}m, {self.peso:.2f}kg"


pessoas = []

while True:

    print("""
        Cadastro de Pessoas
        1 - Cadastrar
        2 - Listar
        3 - Excluir
        4 - Atualizar Cadastro
        5 - Salvar dados
        6 - Carregar dados
        0 - Sair
    """)

    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        altura = float(input("Digite a altura: "))
        peso = float(input("Digite o peso: "))

        pessoas.append(Pessoa(nome, idade, altura, peso))
        print("Pessoa cadastrada!")

    elif opcao == 2:
        if len(pessoas) == 0:
            print("Sem pessoas para exibir.")
        else:
            for pessoa in pessoas:
                print(pessoa.exibir())

    elif opcao == 3:
        if len(pessoas) == 0:
            print("Não tem pessoas para excluir.")
            continue

        nome = input("Digite o nome da pessoa para excluir: ")

        for pessoa in pessoas:
            if pessoa.nome == nome:
                pessoas.remove(pessoa)
                print("Pessoa excluída!")
                break
        else:
            print("Nome não encontrado.")

    elif opcao == 4:
        if len(pessoas) == 0:
            print("Não tem pessoas cadastradas.")
            continue

        nome = input("Digite o nome da pessoa para atualizar: ")

        for pessoa in pessoas:
            if pessoa.nome == nome:
                pessoa.idade = int(input("Digite a nova idade: "))
                pessoa.altura = float(input("Digite a nova altura: "))
                pessoa.peso = float(input("Digite o novo peso: "))

                print("Cadastro atualizado!")
                break
        else:
            print("Nome não encontrado.")

    elif opcao == 5:
        with open("pessoas.pkl", "wb") as arquivo:
            pickle.dump(pessoas, arquivo)

        print("Dados salvos com sucesso!")

    elif opcao == 6:
            try:
                with open("pessoas.pkl", "rb") as arquivo:
                    pessoas = pickle.load(arquivo)
                    print("Dados carregados com sucesso!")
            except FileNotFoundError:
                print("Erro: não foi possível carregar, arquivo não encontrado.")
                continue
    elif opcao == 0:
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida!")