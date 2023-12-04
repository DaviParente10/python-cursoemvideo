soma = 0
cont = 0
for i in range(1,7):
    numero = int(input("Digite um número:"))
    if numero % 2 == 0:
        soma = soma + numero 
        cont = cont + 1
print(f"Soma {soma}, quantidade de valores {cont}")