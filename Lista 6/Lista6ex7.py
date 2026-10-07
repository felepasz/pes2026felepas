'''7 – Utilizando como base o exercício anterior, inclua no menu mais duas opções: uma
para excluir uma pessoa baseada no seu nome e outra para atualizar a idade, altura e
peso, baseado, também, no nome informado.'''

class Pessoa:
    def __init__ (self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def exibir(self):
        return f"{self.nome}, {self.idade} anos, {self.altura:.2f}m, {self.peso:.2f}kg "

pessoas = []

while True:

    print('''
             Casastro de Pessoas
             1 – Cadastrar
             2 – Listar
             3 – Excluir
             4 – Atualizar Cadastro
             0 – Sair
             Opção:
                        ''')
    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        altura = float(input("Digite a altura: "))
        peso = float(input("Digite o peso: "))
        pessoas.append(Pessoa(nome, idade, altura, peso))

    elif opcao == 2:
        if len(pessoas) == 0:
            print("Sem nomes para exibir.")
        else:
            for i in pessoas:
                print(i.exibir())

    elif opcao == 3:
        if len(pessoas) == 0:
            print("Não tem nomes para excluir.")
            continue
        digite = input("Digite o nome da pessoa para excluir: ")
        for i in pessoas:
            if i.nome == digite:
                pessoas.remove(i)
                print("Nome excluido.")
            else:
                print("Nome não encontrado.")
                continue

    elif opcao == 4:

        if len(pessoas) == 0:
            print("Não tem pessoas cadastradas.")
            continue

        nome = input("Digite o nome da pessoa para atualizar: ")

        for i in pessoas:
            if i.nome == nome:
                i.idade = int(input("Digite a nova idade: "))
                i.altura = float(input("Digite a nova altura: "))
                i.peso = float(input("Digite o novo peso: "))

                print("Cadastro atualizado!")
                break
        else:
            print("Nome não encontrado.")

    elif opcao == 0:
        break

    else:
        print("Opção invalida")
        continue
