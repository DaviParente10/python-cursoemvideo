import time
from random import randint
jogador = int(input("Opções \n [0]Pedra\n [1]Papel\n [2]Tesoura"))
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0,2)
print(f"O computador jogou {itens[computador]}")
print(f"Jogador jogou {computador[itens]}")
print('-=' *10)
if computador == 0:
    if jogador == 0:
        print("Empate")
    elif jogador == 1:
        print("Jogador vence.")
    elif jogador == 2:
        ("Jogador perde.")
    else:
        print("Jogada inválida.")
if computador == 1:
    if jogador == 0:
        print("Jogador perdeu.")
    elif jogador == 1:
        print("Empate.")
    elif jogador == 2:
        ("Jogador vence.")
    else:
        print("Jogada inválida.")
if computador == 2:
    if jogador == 0:
        print("Jogador perde.")
    elif jogador == 1:
        print("Jogador vence.")
    elif jogador == 2:
        ("Empate.")
    else:
        print("Jogada inválida.")
else:
    print("Jogada inválida.")