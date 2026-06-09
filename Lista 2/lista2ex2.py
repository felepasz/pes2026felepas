#2 - Faça um programa para escrever a contagem regressiva do lançamento
#de um foguete. O programa deve imprimir 10, 9, 8, ..., 1, 0 e Fogo! na tela.

import time

for segundo in range(10, -1, -1):
    print(segundo)
    time.sleep(1)
# vai iniciar o print "FOGO!" depois de 10 segundos
print("Fogo!")
