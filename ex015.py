kmRodados = float(input("Quantos KM o carro rodou?"))
diasAlugados = int(input("Quantos dias foi alugado?"))
pagar = (60 * diasAlugados) + (0.15 * kmRodados)
print(f"Preço a pagar R${pagar}")