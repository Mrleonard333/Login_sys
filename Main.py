from time import sleep

count = 0
log = None
u = s = None

file = open('Logs.txt', 'r+')
contas = file.readlines()

# Introdução
print('Ola tester!')
sleep(1)
c = str(input('Ja possui uma conta? [S/N] '))
sleep(1)

# Se não possiu uma conta
if c.lower() == 'n':
    print('cadastre-se por favor\n')
    sleep(1)
    u = str(input('Usuario: '))
    s = str(input('Senha: '))
    login = f'{u} {s}\n'

    # Anota no arquivo
    file.write(login)

# Se tem conta
if c.lower() == 's':
    print('Por favor identifique-se\n')
    sleep(1)
    u = str(input('Usuario: '))
    s = str(input('Senha: '))
    login = f'{u} {s}'

    # Enquanto o contador for menor do que a list
    while count < len(contas):
        # Faz a comparação
        if login == contas[count].replace('\n', ''):
            log = True
            break
        else:
            log = False

        count += 1

# Conclusão
if log:
    print(f'[Login concluido]')

elif log is None:
    print('[Cadastrado]')

elif not log:
    print('[*Usuario ou senha incorretos*]')