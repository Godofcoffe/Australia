"""
banquin de dados
Se quisérez pode salvar os dicionarios em um txt...
e adicionar criptografia as pwds
"""
from random import randint

# id:senha
pwds = {}

tmp = []

# usuario:id
users = {}

while True:
    esc = int(input('[ 1 ] Cadastrar\n[ 2 ] Login\n-->:'))

    if esc == 1:
        user = str(input('Usuario: '))
        pwd = str(input('Senha: '))
        for c in range(0, 8):
            tmp.append(str(randint(0, 9)))
        aidi = ''.join(tmp)
        if aidi in users or user in users:
            print('Usuario já existe!')
        else:
            users[user] = aidi
            pwds[user] = pwd
            tmp.clear()
            print('Cadastro feito com sucesso!')

    elif esc == 2:
        user = str(input('Usuario: '))
        pwd = str(input('Senha: '))
        while pwds[user] != pwd:
            print('tente de novo')
            pwd = str(input('Senha: '))
        else:
            print('login aprovado')
            break
# pode adicionar mais coisas aqui
print('nao a oque fazer, ainda em construçao')
print(f'Seu id é {users[user]}')
