from random import shuffle


primeiro = 'Olá'
segundo = 'Mundo'
print(primeiro, segundo)
print(primeiro.upper(), segundo.lower())
print(primeiro.lower(), segundo.upper())
print(primeiro.upper(), segundo.upper())
print(primeiro.lower(), segundo.lower())
print(segundo, primeiro)
palavra = []
l: str
for l in primeiro:
    palavra.append(l)
    for l2 in segundo:
        palavra.append(l2)
print(palavra)
print(''.join(palavra))
tupla = (primeiro, segundo)
print(tupla)
lista = [primeiro, segundo]
print(lista)
dicionario = {primeiro: segundo, segundo: primeiro}
print(dicionario[primeiro], dicionario[segundo])
terceiro = primeiro + segundo
letras = []
for c in range(len(terceiro) - 1, -1, -1):
    nome = primeiro + segundo
    letras.append(terceiro[c])
    print(nome[c], end='')
for d in range(0, len(terceiro)):
    print(f'\n\033[33m{terceiro[d]}\033[m')
shuffle(letras)
for letra in letras:
    print(letra, end='')
