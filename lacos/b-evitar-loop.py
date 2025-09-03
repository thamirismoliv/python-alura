contador = 0

while contador < 10:
    print("Processando dados...")

    #Um loop infinito ocorre quando a condição de parada nunca é alcançada,
    #  fazendo com que o programa fique preso executando o loop indefinidamente.
    #  Para evitar isso, é necessário garantir que o valor do contador seja
    #  atualizado dentro do loop, permitindo que a condição seja eventualmente falsa.

    contador += 1  # Atualiza o contador para evitar loop infinito
print("Processamento concluído!")