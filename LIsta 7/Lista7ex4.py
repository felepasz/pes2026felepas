'''4 - Exercício: Funcionario e ContratoDeTrabalho (1..1).
Objetivo: Modelar um 1..1 onde a "parte" (Contrato) é obrigatória e contém a lógica de
cálculo que o "todo" (Funcionario) utiliza.
Classes: ContratoDeTrabalho e Funcionario.
Regras:
• A classe ContratoDeTrabalho deve ter salario_bruto (float) e percentual_impostos
(float, ex: 0.11 para 11% de INSS).
• O ContratoDeTrabalho deve ter um método chamado valor_impostos que calcula e
retorna o valor exato do desconto (ex: salario_bruto * percentual_impostos).
• A classe Funcionario deve ter nome e cargo.
• Um Funcionario deve ter exatamente um ContratoDeTrabalho para ser criado
(1..1).
• O __init__ do Funcionario deve receber nome, cargo, e também o salario_bruto e o
percentual_impostos necessários para criar sua própria instância de
ContratoDeTrabalho (Composição). O atributo funcionario.contrato nunca pode ser
None.
• Crie um método chamado salario_liquido na classe Funcionario. Este método deve:
◦ Acessar o salario_bruto do seu contrato.
◦ Acessar o valor_impostos calculado pelo seu contrato.
◦ Retornar o salario_bruto menos o valor_impostos.
Seu programa principal deve ter um menu interativo onde se possa testar todos os
métodos de um objeto do tipo Funcionario. Faça, também, o Diagrama de Classes da sua
implementação final.'''

class ContratoDeTrabalho:
    def __init__(self, salario_bruto, percentual_impostos):
        self.salario_bruto = salario_bruto
        self.percentual_impostos = percentual_impostos

    def valor_impostos(self):
        return self.salario_bruto * self.percentual_impostos

    def __repr__(self):
        return f"Salário bruto: R$ {self.salario_bruto:.2f}"


class Funcionario:
    def __init__(self, nome, cargo, salario_bruto, percentual_impostos):
        self.nome = nome
        self.cargo = cargo
        self.contrato = ContratoDeTrabalho(
            salario_bruto, percentual_impostos
        )

    def salario_liquido(self):
        return (
            self.contrato.salario_bruto
            - self.contrato.valor_impostos()
        )

    def __repr__(self):
        return f"Funcionário: {self.nome}, Cargo: {self.cargo}"

nome = input("Digite o nome do funcionário: ")
cargo = input("Digite o cargo do funcionário: ")
salario_bruto = float(input("Digite o salário bruto: R$ "))
percentual_impostos = float(
    input("Digite o percentual de impostos (ex.: 0.11 para 11%): ")
)

funcionario = Funcionario(
    nome, cargo, salario_bruto, percentual_impostos
)

opcao = ""

while opcao != "0":
    print("\n--- MENU ---")
    print("1 - Mostrar dados do funcionário")
    print("2 - Calcular valor dos impostos")
    print("3 - Calcular salário líquido")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print(funcionario)
        print(funcionario.contrato)

    elif opcao == "2":
        impostos = funcionario.contrato.valor_impostos()
        print(f"Valor dos impostos: R$ {impostos:.2f}")

    elif opcao == "3":
        print(f"Salário líquido: R$ {funcionario.salario_liquido():.2f}")

    elif opcao == "0":
        print("Programa encerrado")

    else:
        print("Opção inválida")

        #diagrama nos arquivos enviados