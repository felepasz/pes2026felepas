'''6 – Utilizando como base a classe Pessoa do exercício anterior, crie um algoritmo que
funcionará como um cadastro de pessoas em uma lista. Seu algoritmo deve ter um menu
conforme abaixo:
Cadastro de Pessoas
-------------------
1 – Cadastrar
2 – Listar
0 – Sair
Opção:'''

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
        for i in pessoas:
            print(i.exibir())

    elif opcao == 0:
        break

    else:
        print("Opção invalida")
        continue


