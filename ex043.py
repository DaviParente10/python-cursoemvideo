peso = float(input("Digite seu peso (KG):"))
altura = float(input("Digite sua altura (m):"))
imc = peso / (altura ** 2)
if imc < 18.5:
    print("Abaixo do peso.")
elif 18.5 <= imc < 25:
    print("Faixa de peso normal.")
elif 25 <= imc <30:
    print("Faixa de sobrepeso.")
elif 30 <= imc < 40:
    print("Faixa de obesidade.")
else:
    print("Obesidade mórbida.")