'''3 - VagaDeEstacionamento e Carro (0..1 - Associação Simples)
Objetivo: Modelar um relacionamento 0..1 onde a "parte" (Carro) vem de fora
(Agregação/Associação).
Classes: Carro e VagaDeEstacionamento.
Regras:
A classe Carro é simples, tem apenas placa e modelo.
• A classe VagaDeEstacionamento tem um id_vaga (ex: "A-101").
• Uma VagaDeEstacionamento pode estar ocupada por zero ou um Carro (0..1). O
atributo carro_estacionado começa como None.
• Crie um método ocupar_vaga(carro_obj). Este método deve verificar se a vaga já
está None. Se estiver livre, associa o carro_obj (vindo de fora) à vaga e retorna
True. Se já estiver ocupada, não faz nada e retorna False.
• Crie um método liberar_vaga() que simplesmente seta carro_estacionado de volta
para None.
Seu programa principal deve ter um menu interativo onde se possa testar todos os
métodos de um objeto do tipo VagaDeEstacionamento. Faça, também, o Diagrama de
Classes da sua implementação final.'''


class Carro:
    def __init__(self, placa, modelo):
        self.placa = placa
        self.modelo = modelo

    def __repr__(self):
        return f"Carro: {self.modelo} | Placa: {self.placa}"


class VagaDeEstacionamento:
    def __init__(self, id_vaga):
        self.id_vaga = id_vaga
        self.carro_estacionado = None

    def ocupar_vaga(self, carro_obj):
        if self.carro_estacionado is None:
            self.carro_estacionado = carro_obj
            return True
        else:
            return False

    def liberar_vaga(self):
        self.carro_estacionado = None

id_vaga = input("Digite o ID da vaga: ")
vaga = VagaDeEstacionamento(id_vaga)

while True:
    print("\n--- MENU ESTACIONAMENTO ---")
    print("1 - Consultar vaga")
    print("2 - Ocupar vaga")
    print("3 - Liberar vaga")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        if vaga.carro_estacionado is None:
            print(f"A vaga {vaga.id_vaga} está livre.")
        else:
            print(f"A vaga {vaga.id_vaga} está ocupada.")
            print(vaga.carro_estacionado)

    elif opcao == "2":
        placa = input("Digite a placa do carro: ")
        modelo = input("Digite o modelo do carro: ")

        carro = Carro(placa, modelo)

        if vaga.ocupar_vaga(carro):
            print("Carro estacionado com sucesso")
        else:
            print("A vaga já está ocupada")

    elif opcao == "3":
        if vaga.carro_estacionado is None:
            print("A vaga já está livre.")
        else:
            vaga.liberar_vaga()
            print("Vaga liberada com sucesso")

    elif opcao == "0":
        print("Programa encerrado")
        break

    else:
        print("Opção inválida")

        #diagrama nos arquivos enviados