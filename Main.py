from time import sleep

count = 0
log = False
exi = False
u = s = None

# Importa o arquivo de contas
try:
    file = open('Logs.txt', 'r+')
except:
    file = open('Login_sys/Logs.txt', 'r+')
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
            exi = True
            break

    # Conclusão
    if not exi:
        print('[Cadastrado]')
        file.write(f'{login}\n')

    else:
        print('[*Esta conta ja existe*]')

# Se tem conta
if c.lower() == 's' or c.lower() == 'sim' or c.lower() == 'claro':
    print('\nEntão...')
    sleep(0.6)
    print('Por favor identifique-se')
    sleep(0.5)
    u = str(input('Usuario: '))
    s = str(input('Senha: '))
    login = f'{u} {s}'

    # Enquanto o contador for menor do que a lista
    for c in contas:
        # Faz a comparação
        if login == c.replace('\n', ''):
            log = True
            break

    if log:
        print(f'\n[Login concluido]\n')
        sleep(1)
        c = str(input('Deseja mudar sua senha? [S/N] '))
        sleep(0.5)
        if c.lower() == 's' or c.lower() == 'sim' or c.lower() == 'claro':

            ns = str(input('Senha nova: '))
            cont = 0

            for c in contas:
                if login == c.replace('\n', ''):
                    contas[cont] = f'{u} {ns}\n'

            try:
                with open('Login_sys/Logs.txt', 'w') as file:
                    file.write('')

                with open('Login_sys/Logs.txt', 'r+') as file:
                    for c in contas:
                        file.write(c)
            except:
                with open('Logs.txt', 'w') as file:
                    file.write('')

                with open('Logs.txt', 'r+') as file:
                    for c in contas:
                        file.write(c)

    if not log:
        print(f'[Usuario ou senha incorretos]\n')