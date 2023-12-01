import math

catAdjacente = float(input("Digite o cateto adjacente:"))
catOposto = float(input("Digite o cateto oposto:"))
print(f"Hipotenusa = {(catAdjacente ** 2 + catOposto ** 2) ** (1/2)}")

hi = math.hypot(catAdjacente, catOposto)
print(f"{hi}, com a função Math.")