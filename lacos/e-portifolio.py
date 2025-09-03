# Crie um programa que ajude Ana a percorrer a lista
# de projetos em seu portifólio e exiba os nomes dos projetos válidos.
# Se encontrar um item None, o programa deve exibir
# a mensagem: "Projeto ausente"

projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for projeto in projetos:
    if projeto is None:
        print("Projeto ausente")
    else:
        print(projeto)