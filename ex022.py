
nomeCompleto = str(input("Digite seu nome completo:")).strip()
print(f"Seu nome em maíusculo é {nomeCompleto.upper()}, em minúsculo {nomeCompleto.lower()}. Ao todo {len(nomeCompleto) - nomeCompleto.count(' ')} letras. Primeiro nome {nomeCompleto.find(' ')}")

'''ou'''
separa = nomeCompleto.split()
print(f"Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras")