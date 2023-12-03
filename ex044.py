print(f"{'='*20}Lojas Davi{'='*20}") 
valorProduto = float(input("Digite o valor do produto:"))
pagamento = int(input("Qual será a condição de pagamento?\n [1] À vista dinheiro/cheque \n [2] Cartão \n"))
if pagamento == 1:
    print(f"Valor com 10% de desconto: {valorProduto -(10*valorProduto)/100}")
elif pagamento == 2:
    opcaoCartao = int(input("Selecione:\n [1] À vista no Cartão \n [2] Em até 2x no cartão \n [3] 3x ou mais \n"))
    if opcaoCartao == 1:
        print(f"Você deverá pagar {valorProduto - (5 * valorProduto)/100}")
    elif opcaoCartao == 2:
        print(f"Você deverá pagar o preço normal, de {valorProduto}")
    elif opcaoCartao == 3:
        parcela = int(input("Quantas parcelas?"))
        print(f"Você deverá pagar {parcela} parcelas no valor de  {(valorProduto + (20*valorProduto)/100)/parcela}") 
    else:
        print("Opção inválida.")
else:
        print("Opção inválida.")