#Digite o total de despesas do mês (R$): 5897.58
#ATENÇÃO: Seu orçamento ultrapassou o limite!


orcamento = 3000.00
gastos = float(input("Digite o total de despesas do mês (R$): "))

if gastos > orcamento:
    print("ATENÇÃO: Seu orçamento ultrapassou o limite!")
else:
    print("Seu orçamento está dentro do limite.")
