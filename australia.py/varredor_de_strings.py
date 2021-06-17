lista_palavras = input("Frase: ").lower().split()
ocorrencias = {}


def retificador(lista):
    caracteres_especiais = ['!', ",", ".", "?", "(", ")", ";", ":"]
    for index, l in enumerate(lista):
        for caracter in caracteres_especiais:
            if caracter in l:
                lista[index] = l.replace(caracter, "")
    return lista


num = 1
for palavra in retificador(lista_palavras):
    print(palavra)
    if palavra in ocorrencias.keys():
        num += 1
        ocorrencias[palavra] = num
    else:
        ocorrencias[palavra] = 1
