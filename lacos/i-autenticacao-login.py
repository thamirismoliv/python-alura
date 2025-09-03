while True:
    nome_usuario = input("Digite seu nome de usuario: ")
    senha = input("Digite sua senha: ")

    if len(nome_usuario) < 5:
        print("O nome de usário deve ter pelo menos 5 caracteres")
        continue

    if len(senha) < 8:
        print("A senha deve conter pelo menos 8 caracteres")
        continue

    # A partir daqui, as condições de nome de usuário e senha já foram verificadas
    # e são válidas. A indentação é crucial.
    print("Cadastro realizado com sucesso")
    break