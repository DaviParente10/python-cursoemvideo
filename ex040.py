nota1 = int(input("Digite sua primeira nota:"))
nota2 = int(input("Digite sua segunda nota:"))
media = (nota1+nota2)/2
if media < 5:
    print(f"Reprovado. Média {media}")
elif media > 5 and media < 6.9:
    print(f"Em recuperação. Média {media}")
else:
    print(f"Aluno está aprovado. Média {media}")