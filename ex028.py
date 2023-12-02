'''import random
numero = int(input("Digite um número de 0 a 5:"))
possibilidade = [0,1,2,3,4,5]
if numero > 5 or numero < 0:
    print("Apenas números de 0 a 5!")
escolha = random.choice(possibilidade)
if escolha == numero:
    print("Venceu!")
else:
    print("Perdeu!")'''
from random import randint
from time import sleep
computador = randint(0,5)
jogador = int(input("Número:"))
sleep(2)
if jogador == computador:
    print("Venceu!")
else:
    print("Perdeu!")


