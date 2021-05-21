"""
Em um concurso que tem apenas 1 vaga disponı́vel, 30 candidatos participaram de uma
prova com 20 questões. Para cada questão existem 4 possı́veis alternativas (’A’,’B’,’C’ e
’D’) com apenas uma resposta correta. Cada questão vale um ponto, assim pontuação
geral dos candidatos podem variar de 0 a 20 pontos. A quantidade de acerto nas questões
de 16 a 20 servem para definir quem fica melhor classificado em caso de empate na
pontuação geral. Supõem-se que dois ou mais candidatos nunca terão a mesma pontuação
geral e também a mesma quantidade de questões certas nas questões de 16 a 20. Assim,
por exemplo, se dois candidatos tiverem 15 pontos, eles não terão a mesma quantidade de
acertos nas questões de 16 a 20. Isso significa que um deles acertou mais nas 15 primeiras
e o outros menos nelas, contudo mais nas questões de 16 a 20.
Faça um algoritmo que leia como entrada:
• O gabarito com as respostas corretas das 20 questões da prova.
• Os nomes dos 30 candidatos
• As 20 respostas dos 30 candidatos
Seu programa deve exibir como saı́da
A) A porcentagem de candidatos em cada uma das pontuações possı́veis (de 0 a 20);
B) A porcentagem de acertos em cada um das questões;
C) O nome e a pontuação de cada candidato;
D) O nome do candidato que obteve a melhor pontuação. Em caso de empate na pon-
tuação geral, lembre-se de verificar a pontuação das questões de 16 a 20.
"""

from random import choice
print('Gabarito das questões:')
print('-'*40)
resps = {}
for c in range(1, 21):
    alternativa = str(input(f'Alternativa da questão {c}: ')).upper()
    while alternativa not in 'ABCD' or not alternativa:
        alternativa = str(input(f'Por Favor!\nAlternativa da questão {c}: ')).upper()
    resps[f'Questão {c}'] = alternativa

print()
print('Nomes dos candidatos:')
print('-'*40)
candidatos = []
for c in range(1, 31):
    linha = []
    alternativas = []
    nome = str(input(f'Nome do {c}° candidato: '))
    print(nome)
    valid = str(input('Você tem certeza? [s/n]: '))
    while valid == 'n':
        nome = str(input(f'Nome do {c}° candidato: '))
        valid = input('Você tem certeza? [s/n]: ')
    while valid != 's':
        valid = input('Você tem certeza? [s/n]: ')
    linha.append(nome)
    for d in range(1, 21):
        pnt = int(input(f'Resposta da Questão {d}: ')).upper()
        valid = str(input('Você tem certeza? [s/n]: '))
        while pnt not in 'ABCD' or not pnt:
            pnt = str(input(f'Por Favor!\nA Resposta da questão {c}: ')).upper()
        while valid == 'n':
            pnt = str(input(f'Resposta da Questão {d}: ')).upper()
            valid = input('Você tem certeza? [s/n]: ')
        while valid != 's':
            valid = input('Você tem certeza? [s/n]: ')
        alternativas.append(pnt)
        linha.append(nome, alternativas)
    candidatos.append(linha)

print(resps)
print(candidatos)
porcent_pnt = {}
for pessoa in candidatos:
    for c in range(21):
        if c in pessoa[1]:
            porcent_pnt[f'{c}'] += 1

print(porcent_pnt)
