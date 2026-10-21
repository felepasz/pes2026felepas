
''',
2 - Exercício 2: Computador e CPU (1..1).
Objetivo: Implementar um relacionamento obrigatório (Composição).
Classes: CPU e Computador.
Regras:
A classe CPU deve ter atributos fabricante (ex: "Intel") e modelo (ex: "i7-12700K").
• A classe Computador deve ter um atributo tipo (ex: "Desktop" ou "Notebook").
• Um Computador deve ter exatamente uma CPU para ser criado (1..1).
• O __init__ do Computador deve receber os dados necessários para criar sua
própria instância de CPU. O atributo computador.cpu nunca pode ser None.
Comprove o funcionamento da sua implementação no programa principal.
Veja, na figura abaixo, o Diagrama de Classes completo:'''

class CPU:
    def __init__(self, fabricante, modelo):
        self.fabricante = fabricante
        self.modelo = modelo

    def __repr__(self):
        return f"CPU: {self.fabricante} {self.modelo}"


class Computador:
    def __init__(self, tipo, fabricante, modelo):
        self.tipo = tipo
        self.cpu = CPU(fabricante, modelo)

    def __repr__(self):
        return f"Computador: {self.tipo} | {self.cpu}"

computador1 = Computador("Desktop", "Intel", "i7-12700K")

print(computador1)

