valor1 = float(input("Digite o primeiro valor:"))
valor2 = float(input("Digite o segundo valor"))
if valor1 > valor2: 
    print(f"O primeiro valor {valor1} é maior")
elif valor2 < valor1: 
    print(f"O segundo valor, {valor2} é maior.") 
else:
    print(f"Números iguais. Ambos são {valor1}.")