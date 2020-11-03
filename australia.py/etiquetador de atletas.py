from datetime import date

"""Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
"""
ano_atual = date.today().year
nascimento = int(input('Digite o ano de nascimento do atleta:'))
idade = ano_atual - nascimento
print(f'O(A) Atleta tem {idade} anos')
if idade <= 9:
    print(f'Com a idade de {idade}, ele(a) é MIRIN.')
elif idade <= 14:
    print(f'Com a idade de {idade}, ele(a) é INFANTIL.')
elif idade <= 19:
    print(f'Com a idade de {idade}, ele(a) é JÚNIOR')
elif idade <= 25:
    print(f'Com a idade de {idade}, ele(a) é SÊNIOR.')
else:
    print(f'Com a idade de {idade}, ele(a) é MASTER.')
