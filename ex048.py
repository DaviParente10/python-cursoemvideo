soma = 0
cont = 0
for i in range(1,501):
    if i % 3 == 0:
        soma = soma + i
        cont = cont + 1
print(f"A soma de {cont} valores citados é {soma}")