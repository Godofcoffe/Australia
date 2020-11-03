"""Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos. """
idade_velho = 0
nome_velho = 'null'
mulheres = 0
media = 0
for p in range(1, 5):
    print(f'-----/ {p}° PESSOA /-----')
    pessoa = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('sexo M/F: ')).lower().strip()
    media += idade
    if p == 1 and sexo == 'm':
        idade_velho = idade
    if idade > idade_velho and sexo == 'm':
        idade_velho = idade
        nome_velho = pessoa
    if sexo == 'f' and idade < 20:
        mulheres += 1
print(f'A media do total da idade das 4 pessoas é de {media / 4:.1f}')
print(f'O homem mais velho é {nome_velho} com a idade de {idade_velho}')
print(f'A {mulheres} mulher(es) menores de 20 anos.')
