primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
padrao = 10
c = 0
continuar = True
while c < padrao and continuar:
    if c == padrao - 1:
        print('ACABOU...')
        con = int(input('\nDigite outra razão para continuar... \n[ 0 ] para fechar:'))
        if con == 0:
            print('')
            continuar = False
            print('Fechando...')
        else:
            print('')
            print('-=' * 60)
            padrao = con + 1
            c = 0
    else:
        print(f'{primeiro}', end=' ---> ')
    c += 1
    primeiro += razao
