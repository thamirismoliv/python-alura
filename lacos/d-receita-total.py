# Você está recebendo uma lista de valores representando os
# produtos de sua loja virtual e gostaria de calcular a soma
# total desses produtos para entender o desempenho financeiro semanal.

numeros = [10, 20, 30, 40, 50]

soma = 0 
for numero in numeros:
    soma += numero  # Adiciona o número atual à soma total
    print(f"A soma total das receitas é: {soma}")
