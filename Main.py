from time import sleep

count = 0
log = None
u = s = None

# Importa o arquivo de contas
file = open('Logs.txt', 'r+')
contas = file.readlines()

# Introdução
print('Ola tester')
sleep(0.5)
print('Seja bem vindo ao meu sistema de login\n')
sleep(1)
c = str(input('Ja possui uma conta? [S/N] '))
sleep(1)

# Se não possui uma conta
if c.lower() == 'n' or c.lower() == 'não' or c.lower() == 'nao':
    print('\ncadastre-se por favor')
    sleep(1)
    u = str(input('Usuario: '))
    s = str(input('Senha: '))
    login = f'{u} {s}'

    # Verifica o usuario e senha
    for c in contas:
        if login == c.replace('\n', ''):
            print('[*Esta conta ja existe*]')

        else:
            print('[Cadastrado]')
            file.write(f'{login}\n')

# Se tem conta
if c.lower() == 's' or c.lower() == 'sim' or c.lower() == 'claro':
    print('\nEntão...')

    sleep(0.8)

    print('Por favor identifique-se')
    u = str(input('Usuario: '))
    s = str(input('Senha: '))
    login = f'{u} {s}'

    # Enquanto o contador for menor do que a lista
    for c in contas:
        # Faz a comparação
        if login == c.replace('\n', ''):
            log = True
        else:
            log = False

# Conclusão
if log:
    print(f'[Login concluido]')

elif not log:
    print('[*Usuario ou senha incorretos*]')