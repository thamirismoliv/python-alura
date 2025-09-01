'''Digite seu peso (kg): 75
Digite sua altura (m): 1.68
Seu IMC é 26.57
Seu peso está na categoria: Sobrepeso '''

peso = float(input("Digite seu peso (kg): ")) 
altura = float(input("Digite sua altura (m): ")) 

imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Seu peso está na categoria: Abaixo do peso")

elif imc < 25:
    print("Seu peso está na categoria: Peso normal")

else:
    print("Seu peso está na categoria: Sobrepeso")