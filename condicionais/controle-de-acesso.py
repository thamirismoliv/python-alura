# Digite a hora atual (formato 24h): 21
# Acesso negado. Fora do horário permitido.

hora_atual = int(input("Digite a hora atual (formato 24h): "))

if 8 <= hora_atual < 18:
    print("Acesso permitido.")
else: print("Acesso negado. Fora do horário permitido.")
