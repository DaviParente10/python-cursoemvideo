#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
numero = int(input("Número:"))
razao = int(input("Digite a razão:"))
decimo = numero + (10-1) * razao
for i in range(numero,decimo + razao, razao):
    print(i,end='->')
print("\nAcabou")