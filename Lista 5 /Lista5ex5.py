'''5 – Programe um algoritmo com mais algumas funções úteis para a manipulação de listas
numéricas:
a) uma função que receba uma lista e retorne True, caso esteja vazia, ou False, caso
possua um ou mais elementos;
b) uma função que receba uma lista e retorne o maior valor;
c) uma função que receba uma lista e retorne o menor valor;
d) uma função que receba uma lista e retorne o valor médio.
As funções dos itens b, c e d devem retornar -1 caso a lista esteja vazia. No seu
programa principal, crie duas listas (uma vazia e outra com alguns elementos) e teste
(comprove) o funcionamento de cada uma das funções.'''

def lista_vazia(lista):
    if len(lista) == 0:
        return True
    else:
        return False


def maior_valor(lista):
    if lista_vazia(lista):
        return -1
    return max(lista)


def menor_valor(lista):
    if lista_vazia(lista):
        return -1
    return min(lista)


def valor_medio(lista):
    if lista_vazia(lista):
        return -1
    return sum(lista) / len(lista)

lista_vazia_teste = []
lista_com_elementos = [10, 5, 20, 15, 30]

print("LISTA VAZIA:", lista_vazia_teste)
print("Está vazia?", lista_vazia(lista_vazia_teste))
print("Maior valor:", maior_valor(lista_vazia_teste))
print("Menor valor:", menor_valor(lista_vazia_teste))
print("Valor médio:", valor_medio(lista_vazia_teste))

print("\n-------------------------\n")

print("LISTA COM ELEMENTOS:", lista_com_elementos)
print("Está vazia?", lista_vazia(lista_com_elementos))
print("Maior valor:", maior_valor(lista_com_elementos))
print("Menor valor:", menor_valor(lista_com_elementos))
print("Valor médio:", valor_medio(lista_com_elementos))