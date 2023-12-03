valorCasa = float(input("Valor da casa:"))
salarioComprador = float(input("Salário do comprador:"))
anosPagar = int(input("Em quantos anos vai pagar:"))
prestacao = valorCasa / (anosPagar*12)
if prestacao <= salarioComprador * 30 / 100:
    print("Empréstimo pode ser concedido.")
else:
    print("Empréstimo não pode ser concedido.")