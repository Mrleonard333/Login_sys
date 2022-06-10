from time import sleep

count = 0
log = None
u = s = None

file = open('Logs.txt', 'r+')
contas = file.readlines()

print('Ola tester!')
sleep(1)
c = str(input('Ja possui uma conta? [S/N] '))
sleep(1)

if c.lower() == 'n':
    print('cadastre-se por favor\n')
    sleep(1)
    u = str(input('Usuario: '))
    s = str(input('Senha: '))
    login = f'{u} {s}\n'

    file.write(login)

if c.lower() == 's':
    print('Por favor identifique-se\n')
    sleep(1)
    u = str(input('Usuario: '))
    s = str(input('Senha: '))
    login = f'{u} {s}'

    while count < len(contas):
        if login == contas[count].replace('\n', ''):
            log = True
            break
        else:
            log = False

        count += 1

if log:
    print(f'[Login concluido]')

elif log is None:
    print('[Cadastrado]')

elif not log:
    print('[*Usuario ou senha incorretos*]')