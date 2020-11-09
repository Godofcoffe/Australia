# 5° 58′ 41,191″ N, 75° 25′ 05,28″
times = ('Internacional', 'Atlético_MG', 'Flamengo', 'São Paulo', 'Fluminense',
         'Palmeras', 'Santos', 'Grêmio', 'Sport Recife', 'Corinthians', 'Fortaleza',
         'Ceará SC', 'Atlético-GO', 'Bahia', 'Coritiba', 'Bragantino-SP', 'Botafogo',
         'Vasco', 'Athetico-PR', 'Goiás')
print('Os top5 são...')
for c in range(0, 5):
    print(f'{times[c]}', end=', ')
print('\n\nOs perdedores são...')
for c in range(4, 0, -1):
    print(f'{times[-c]}', end=', ')
print('\n\nOs times em ordem alfabetica fica assim...')
print(sorted(times))
print('\nE a Chapecoense está nessa posisão...')
print('5° 58′ 41,191″ N, 75° 25′ 05,28″')
