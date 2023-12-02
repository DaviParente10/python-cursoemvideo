frase = str(input("Digite uma frase:")).strip().lower()
print(f"Quantidade de letras 'A' {frase.count('a')}")
print(f"Primeira ocorrência de 'A'{frase.find('a')+1}e última ocorrência {frase.rfind('a')+1}")
