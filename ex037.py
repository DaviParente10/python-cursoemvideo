numero = int(input("Digite um número inteiro:"))
escolha = int(input("Escolha \n [1] Para binário \n [2] Para Octal \n [3] Para Hexadecimal\n"))
print(f"Sua escolha foi a {escolha}ª! \n")
if escolha == 1:
    print(f"Em binário: {bin(numero)[2:]}")
elif escolha == 2:
    print(f"Em octal{oct(numero)[2:]}")
elif escolha == 3:
    print(f"Em hexadecimal {hex(numero)[2:]}")
else:
    print("Escolha inválida. Tente novamente.")