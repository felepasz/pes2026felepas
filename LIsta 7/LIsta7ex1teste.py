
class MarcadorDePagina:
    def __init__(self, pagina_atual):
        self.pagina_atual = pagina_atual

    def __repr__(self):
        return f"Marcador na página {self.pagina_atual}"


class Livro:
    def __init__(self, titulo, total_paginas):
        self.titulo = titulo
        self.total_paginas = total_paginas
        self.marcador = None

    def adicionar_marcador(self, pagina):
        if self.marcador is None:
            self.marcador = MarcadorDePagina(pagina)
        else:
            self.marcador.pagina_atual = pagina

    def __repr__(self):
        return f"Livro: {self.titulo}, Total de páginas: {self.total_paginas}, Marcador: {self.marcador}"


# Programa principal
titulo = input("Digite o nome do livro: ")
total_paginas = int(input("Digite o total de páginas: "))

livro = Livro(titulo, total_paginas)

while True:
    print("\n1 - Adicionar ou atualizar marcador")
    print("2 - Mostrar informações do livro")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        pagina = int(input("Em qual página deseja deixar o marcador? "))

        if pagina < 1 or pagina > livro.total_paginas:
            print("Página inválida!")
        else:
            livro.adicionar_marcador(pagina)
            print("Marcador atualizado com sucesso!")

    elif opcao == "2":
        print(livro)

    elif opcao == "0":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")

