#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
total = 0
numero = int(input("Digite um número:"))
for i in range(1, numero + 1):
    if numero % i == 0:
        print(f"\033[34m", end='')
        total = total + 1
    else:
        print("\033[31m", end='')
    print(f"{i}", end=' ' )
print(f"\n\033[mO número {numero} foi dividido {total} vezes.")
if total == 2:
    print("E por isso ele é primo!")
else:
    print("E por isso ele não é primo.")