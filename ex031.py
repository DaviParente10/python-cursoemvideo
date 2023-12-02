distancia = float(input("Digite a distância da viagem:"))
if distancia <= 200:
    precoPassagem = distancia * 0.45
else:
    precoPassagem = distancia * 0.50
print(f"O preço a ser pago é  R${precoPassagem} reais.")