#6 - Modifique o programa anterior de forma que o usuário também digite o início e o fim da
#tabuada, em vez de começar iniciar no 1 e terminar no 10.


num = int(input("Selecione um numero: "))

i = int(input("Selecione um numero para começar: "))

x = int(input("Selecione um numero para terminar: "))


if i<x:
    while i <= x: 
     resultado = num*i
     msg = f"{num} X {i} = {resultado}"
     print(msg)
     i = i + 1
     
else:
    while i >= x: 
        resultado = num*i
        msg = f"{num} X {i} = {resultado}"
        print(msg)
        i = i - 1