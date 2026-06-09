#11 – Faça um programa para controlar o caixa de uma cantina. Seu programa deve
#solicitar ao usuário o código do produto pedido e a quantidade comprada. Suponha que
#para cada compra, apenas um tipo de produto possa ser comprado. O programa deve ser
#interrompido caso o usuário digite 0. Para cada compra, seu programa deve exibir na tela
#o nome do produto comprado e o valor total da compra. Ao final do programa, deve exibir
#o valor total acumulado no caixa. Utilize a seguinte tabela de produtos como referência:
#Código Produto Valor
#1 Suco R$ 6,00
#2 Pão de queijo R$ 3,00
#3 Pastel R$ 7,00
#4 Salada de frutas R$ 9,00
#5 Café com leite R$ 3,50
#6 Cappuccino R$ 4,50
#7 Iogurte R$ 6,50
#8 Água R$ 2,50

totalcaixa = 0

while True:
    codigo = int(input("digite o código do produto (0 para sair): "))

    if codigo == 0:
        break

    quantidade = int(input("digite a quantidade: "))

    if codigo == 1:
        produto = "suco"
        preco = 6.00
    elif codigo == 2:
        produto = "pão de queijo"
        preco = 3.00
    elif codigo == 3:
        produto = "pastel"
        preco = 7.00
    elif codigo == 4:
        produto = "salada de frutas"
        preco = 9.00
    elif codigo == 5:
        produto = "café com leite"
        preco = 3.50
    elif codigo == 6:
        produto = "cappuccino"
        preco = 4.50
    elif codigo == 7:
        produto = "iogurte"
        preco = 6.50
    elif codigo == 8:
        produto = "água"
        preco = 2.50
    else:
        print("código inválido!")
        continue

    valorcompra = preco * quantidade
    totalcaixa += valorcompra

    print("produto:", produto)
    print("valor da compra: R$", valorcompra)

print("\nvalor total acumulado no caixa: R$", totalcaixa)