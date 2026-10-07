'''5 – Crie uma classe chamada Pessoa com:
• Atributos: nome, idade, altura e peso;
• Um método para exibir, em uma única linha, o nome, a idade, a altura e o peso da
pessoa;
• Um método para retornar o IMC (Índice de Massa Corpórea) calculado da pessoa;
• Um método para retornar apenas o nome e o IMC da pessoa (em uma única linha).
Teste criando 3 pessoas com diferentes atributos e verificando se os IMCs calculados
estão corretos.'''

class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def exibir(self):
        print(f"{self.nome}, {self.idade} anos, {self.altura}m, {self.peso}kg")

    def imc(self):
        return self.peso / (self.altura * self.altura)

    def nome_imc(self):
        return f"{self.nome} - IMC: {self.imc():.2f}"


nome = input("Nome da pessoa 1: ")
idade = int(input("Idade: "))
altura = float(input("Altura: "))
peso = float(input("Peso: "))

pessoa1 = Pessoa(nome, idade, altura, peso)


nome = input("Nome da pessoa 2: ")
idade = int(input("Idade: "))
altura = float(input("Altura: "))
peso = float(input("Peso: "))

pessoa2 = Pessoa(nome, idade, altura, peso)


nome = input("Nome da pessoa 3: ")
idade = int(input("Idade: "))
altura = float(input("Altura: "))
peso = float(input("Peso: "))

pessoa3 = Pessoa(nome, idade, altura, peso)


pessoa1.exibir()
print(pessoa1.nome_imc())

pessoa2.exibir()
print(pessoa2.nome_imc())

pessoa3.exibir()
print(pessoa3.nome_imc())
