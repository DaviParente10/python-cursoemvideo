velocidade = float(input("Digite a velocidade do carro:"))
if velocidade > 80:
    print(f"Multado em R${(velocidade - 80) * 7.00:.2f} reais. ")
print("Tenha um bom dia! Dirija com segurança!")