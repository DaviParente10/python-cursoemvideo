from datetime import date
anoAtual = date.today().year
anoNascimento = int(input("Digite o seu ano de nascimento:"))
idade = anoAtual - anoNascimento
print(f"O atleta tem {idade} anos.")
if idade <= 9:
    print("Mirim.")
elif idade <=14:
    print("Infantil.")
elif idade <=19:
    print("Classificação Junior.")
elif idade <= 25:
    print("Classificação Sênior.")
else:
    print("Classificação Master.")
