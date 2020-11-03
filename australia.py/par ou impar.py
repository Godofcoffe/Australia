from random import randint, choice

print('-' * 50)
print('Vamos jogar par ou ímpar!')
print('Vou escolher um número de 1 a 10...\nPRONTO?')
opcoes = ['par', 'impar']
vitorias = 0
derrotas = 0
while True:
    usuario = str(input('Seu número: ')).strip()
    valid = usuario.isnumeric()
    if valid and 0 < int(usuario) <= 10:
        escolha = str(input('Par ou Ímpar?  [P/I] ')).lower().strip()
        print('.' * 50)
        print('\n\n\n')
        if escolha in 'parimpar':
            cpu = randint(1, 10)
            cpu_esc = choice(opcoes)
            soma = int(usuario) + cpu
            print(f'O total foi {soma}')
            if escolha == 'p':
                print(f'Você escolheu par...')
            elif escolha == 'i':
                print('Você escolheu impar...')
            else:
                print(f'Você escolheu {escolha}...')
            print(f'Eu escolhi {cpu} e achei que seria {cpu_esc}...')
            print('=' * 15)

            if soma % 2 == 0:
                print(f'{soma} é par')
                if (escolha == 'par' or escolha == 'p') and cpu_esc == 'par':
                    print('Empatamos...')
                    vitorias = 0
                elif escolha == 'par' or escolha == 'p':
                    print('Você ganhou!')
                    vitorias += 1
                    derrotas = 0
                elif cpu_esc == 'par':
                    print('Eu ganhei!')
                    vitorias = 0
                    derrotas += 1
                else:
                    print('Perdemo!')
                    vitorias = 0
                    derrotas += 1
            else:
                print(f'{soma} é ímpar')
                if (escolha == 'impar' or escolha == 'i') and cpu_esc == 'impar':
                    print('Empatamos...')
                    vitorias = 0
                elif escolha == 'impar' or escolha == 'i':
                    print('Você ganhou!')
                    vitorias += 1
                    derrotas = 0
                elif cpu_esc == 'impar':
                    print('Eu ganhei!')
                    vitorias = 0
                    derrotas += 1
                else:
                    print('Perdemo!')
                    vitorias = 0
                    derrotas += 1
        else:
            print('Escolha se acha que irá ser par ou ímpar no total'.upper())
            escolha = str(input('Par ou Ímpar? [P/I] ')).lower().strip()
        print('')
        print('=' * 50)
    else:
        print('Digite somente números e que ele seja menor ou igual que 10'.upper())
        usuario = str(input('Seu número: ')).strip()
        print('-' * 50)
    if vitorias >= 5:
        print(f'Você ganhou com {vitorias} vitorias consecutivas!\nARRASOU!')
    else:
        print(f'Você ganhou com {vitorias} vitorias consecutivas.')
    if derrotas >= 5:
        print(f'Sou vitorioso, você perdeu {derrotas} seguidas, Sou IMBATIVEL.\nBoa Sorte na Proxima.')
        break
    else:
        print(f'Você perdeu {derrotas} seguidas...')
