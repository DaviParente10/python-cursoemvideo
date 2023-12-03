salario = float(input("Salário:"))
if salario <= 1.250:
    salarioAjustado = ((15*salario)/100) + salario
else:
    salarioAjustado = ((10*salario)/100) + salario
print(f"Salário Ajustado: R${salarioAjustado} reais.")