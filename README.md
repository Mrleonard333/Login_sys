# [Login_sys]
## **sistema de login simples**
### Nele, além de se cadastrar e logar, você vai poder Mudar de senha
- ## [**Logar**](#exemplo-logando)
- ## [**Mudar a senha**](#exemplo-mudando-a-senha)
- ## [**Cadastrar**](#exemplo-se-cadastrando)


## Exemplo logando
```
|========================================================|
    Ola tester
    Seja bem vindo ao meu sistema de login

    Ja possui uma conta? [S/N] Sim

    Então...
    Por favor identifique-se
    Usuario: nameless
    Senha: passless

    [Login concluido]

    Deseja mudar sua senha? [S/N] não
 --------------------------------------------------------
     for c in contas:
        if login == c.replace('\n', ''):
            exi = True |- indicador que a conta existe
            break
|========================================================|
```

## Exemplo (mudando a senha)
```
|========================================================|
  [Login concluido]

  Deseja mudar sua senha? [S/N] sim
  Senha nova: passless2
 --------------------------------------------------------
    try:
        with open('Login_sys/Logs.txt', 'w') as file:
            file.write('') |- apagando o texto

        with open('Login_sys/Logs.txt', 'r+') as file:
            for c in contas:
                file.write(c) |- reescrevendo
    except:
        with open('Logs.txt', 'w') as file:
            file.write('')

        with open('Logs.txt', 'r+') as file:
            for c in contas:
                file.write(c)
|========================================================|
```

## Exemplo (se cadastrando)
```
|========================================================|
  Ola tester
  Seja bem vindo ao meu sistema de login

  Ja possui uma conta? [S/N] não

  cadastre-se por favor
  Usuario: random
  Senha: random
  [Cadastrado]
 --------------------------------------------------------
    for c in contas:
        if login == c.replace('\n', ''):
            exi = True |- indicador que a conta existe
            break

    if not exi:
        print('[Cadastrado]')
        file.write(f'{login}\n')

    else:
        print('[*Esta conta ja existe*]')
|========================================================|
```
