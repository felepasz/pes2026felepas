'''8 – Implemente um algoritmo com as duas classes definidas logo abaixo. Seu algoritmo
deve ter um menu com as seguintes opções:
Sistema de Cadastro
-------------------
1 – Cadastrar estudante
2 – Cadastrar professor
3 – Listar estudantes
4 – Listar professores
5 – Alterar estudante pela matrícula
6 – Alterar estudante pelo nome
7 – Alterar professor pela matrícula
8 – Alterar professor pelo nome
9 – Excluir estudante pela matrícula
10 – Excluir professor pela matrícula
0 – Sair
Opção:'''

class estudante:

    def __init__(self, nome, matricula, idade, curso):
        self.nome = nome
        self.matricula = matricula
        self.idade = idade
        self.curso = curso

    def exibir(self):
        return f"Matrícula: {self.matricula} , {self.nome} , {self.idade} anos, Curso: {self.curso}"


class professor:

    def __init__(self, nome, matricula, idade, disciplina):
        self.nome = nome
        self.matricula = matricula
        self.idade = idade
        self.disciplina = disciplina

    def exibir(self):
        return f"Matrícula: {self.matricula}, {self.nome}, {self.idade} anos, Disciplina: {self.disciplina}"


estudantes = []
professores = []


while True:

    print("""
    Sistema de Cadastro
    -------------------

    1 - Cadastrar estudante
    2 - Cadastrar professor
    3 - Listar estudantes
    4 - Listar professores
    5 - Alterar estudante pela matrícula
    6 - Alterar estudante pelo nome
    7 - Alterar professor pela matrícula
    8 - Alterar professor pelo nome
    9 - Excluir estudante pela matrícula
    10 - Excluir professor pela matrícula
    0 - Sair
    """)

    opcao = int(input("Opção: "))

    if opcao == 1:

        nome = input("Digite o nome: ")
        matricula = input("Digite a matrícula: ")
        idade = int(input("Digite a idade: "))
        curso = input("Digite o curso: ")
        estudantes.append(estudante(nome, matricula, idade, curso))
        print("Estudante cadastrado!")

    elif opcao == 2:

        nome = input("Digite o nome: ")
        matricula = input("Digite a matrícula: ")
        idade = int(input("Digite a idade: "))
        disciplina = input("Digite a disciplina: ")
        professores.append(professor(nome, matricula, idade, disciplina))
        print("Professor cadastrado!")

    elif opcao == 3:

        if len(estudantes) == 0:
            print("Não existem estudantes cadastrados.")
            continue
        for i in estudantes:
            print(i.exibir())

    elif opcao == 4:

        if len(professores) == 0:
            print("Não existem professores cadastrados.")
            continue
        for i in professores:
            print(i.exibir())

    elif opcao == 5:

        matricula = input("Digite a matrícula do estudante: ")
        for i in estudantes:
            if i.matricula == matricula:
                i.nome = input("Digite o novo nome: ")
                i.idade = int(input("Digite a nova idade: "))
                i.curso = input("Digite o novo curso: ")
                print("Estudante atualizado!")
                break

        else:
            print("Matrícula não encontrada.")

    elif opcao == 6:

        nome = input("Digite o nome do estudante: ")
        for i in estudantes:
            if i.nome == nome:
                i.matricula = input("Digite a nova matrícula: ")
                i.idade = int(input("Digite a nova idade: "))
                i.curso = input("Digite o novo curso: ")
                print("Estudante atualizado!")
                break

        else:
            print("Nome não encontrado.")

    elif opcao == 7:

        matricula = input("Digite a matrícula do professor: ")
        for i in professores:
            if i.matricula == matricula:
                i.nome = input("Digite o novo nome: ")
                i.idade = int(input("Digite a nova idade: "))
                i.disciplina = input("Digite a nova disciplina: ")
                print("Professor atualizado!")
                break

        else:
            print("Matrícula não encontrada.")

    elif opcao == 8:

        nome = input("Digite o nome do professor: ")
        for i in professores:
            if i.nome == nome:
                i.matricula = input("Digite a nova matrícula: ")
                i.idade = int(input("Digite a nova idade: "))
                i.disciplina = input("Digite a nova disciplina: ")
                print("Professor atualizado!")
                break

        else:
            print("Nome não encontrado.")

    elif opcao == 9:

        matricula = input("Digite a matrícula do estudante: ")
        for i in estudantes:
            if i.matricula == matricula:
                estudantes.remove(i)
                print("Estudante excluído!")
                break

        else:
            print("Matrícula não encontrada.")

    elif opcao == 10:

        matricula = input("Digite a matrícula do professor: ")
        for i in professores:
            if i.matricula == matricula:
                professores.remove(i)
                print("Professor excluído!")
                break

        else:
            print("Matrícula não encontrada.")

    elif opcao == 0:

        break

    else:

        print("Opção invalida.")