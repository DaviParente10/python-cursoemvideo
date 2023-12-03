from datetime import date
anoNascimento = int(input("Digite o ano de nascimento:"))
anoAtual = date.today().year
idade = anoAtual - anoNascimento

if idade == 18:
    print("Você deve se alistar imediatamente.")
elif idade < 18:

    print(f"Você ainda não tem 18 anos. Faltam {18 - idade} anos para o alistamento.")
else:
    print(f"Você já deveria ter se alistado há {idade - 18} anos.")