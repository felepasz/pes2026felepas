'''11 – Crie um algoritmo com uma função que retorna um valor em reais escrito por
extenso. Por exemplo, caso seja passado “1.74” como parâmetro para a função, ela deve
retornar: um real e setenta e quatro centavos. Caso seja passado “3251.90”, deve retornar
“três mil duzentos e cinquenta e um reais e noventa centavos”.'''

def numero_por_extenso(numero):
    unidades = [
        "zero", "um", "dois", "três", "quatro",
        "cinco", "seis", "sete", "oito", "nove"
    ]

    especiais = {
        10: "dez",
        11: "onze",
        12: "doze",
        13: "treze",
        14: "quatorze",
        15: "quinze",
        16: "dezesseis",
        17: "dezessete",
        18: "dezoito",
        19: "dezenove"
    }

    dezenas = [
        "", "", "vinte", "trinta", "quarenta",
        "cinquenta", "sessenta", "setenta",
        "oitenta", "noventa"
    ]

    centenas = [
        "", "cento", "duzentos", "trezentos",
        "quatrocentos", "quinhentos", "seiscentos",
        "setecentos", "oitocentos", "novecentos"
    ]

    if numero < 10:
        return unidades[numero]

    if numero < 20:
        return especiais[numero]

    if numero < 100:
        dezena = numero // 10
        unidade = numero % 10

        if unidade == 0:
            return dezenas[dezena]

        return dezenas[dezena] + " e " + unidades[unidade]

    if numero < 1000:
        if numero == 100:
            return "cem"

        centena = numero // 100
        resto = numero % 100

        if resto == 0:
            return centenas[centena]

        return centenas[centena] + " e " + numero_por_extenso(resto)

    if numero < 1000000:
        milhares = numero // 1000
        resto = numero % 1000

        if milhares == 1:
            resultado = "mil"
        else:
            resultado = numero_por_extenso(milhares) + " mil"

        if resto > 0:
            resultado += " " + numero_por_extenso(resto)

        return resultado


def valor_em_reais(valor):
    valor = float(valor)

    reais = int(valor)
    centavos = round((valor - reais) * 100)

    if reais == 1:
        texto_reais = "um real"
    else:
        texto_reais = numero_por_extenso(reais) + " reais"

    if centavos == 0:
        return texto_reais

    if centavos == 1:
        texto_centavos = "um centavo"
    else:
        texto_centavos = numero_por_extenso(centavos) + " centavos"

    return texto_reais + " e " + texto_centavos


valor = input("Digite um valor em reais: ")

print(valor_em_reais(valor))