while True:
    usuario = input('Entre com o nome de usuário: ')
    senha = input('Entre com a senha: ')
    if (usuario == senha):
        print('Usuário não pode ser igual a senha, tente novamente.')
    else:
        print('Bem vindo')
        break