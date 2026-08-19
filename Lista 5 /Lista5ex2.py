'''2 – Elabore um algoritmo com uma função que retorne se um dado número é par ou
ímpar. Seu programa deve solicitar um número ao usuário, chamar a função e exibir o
resultado na tela.'''

def impapa (a):
    p = a%2
    if p == 0:
     s = ("é par")
    else:
        s = ("é impar")
     
    return s
        
num = int(input("Digite o numero: "))

s2 = impapa(num)
    
print(s2)