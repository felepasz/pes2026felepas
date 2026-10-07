'''4 – Crie uma classe chamada Produto com:
• Atributos: nome e quantidade.
• Um método chamado esta_disponivel que retorna True se a quantidade for maior
que 0 e False caso contrário.
• Um método chamado vender que diminui a quantidade em 1.
Teste criando um objeto, verificando a disponibilidade, vendendo produtos e verificando
novamente.'''

class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade
        
    def esta_disponivel(self):
        if self.quantidade > 0:
            return True
        else:
            return False

    def vender(self):
        self.quantidade -= 1
        
n = input("Nome: ")
q = float(input("Quantidade: "))

produto1 = Produto(n, q)

print(produto1.esta_disponivel())

produto1.vender()

print(produto1.esta_disponivel())
print(f"A quantidade atual é {produto1.quantidade}")