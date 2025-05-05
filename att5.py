soma = 0
quantidade = 0

while True:
    n = float(input("Digite um número (maior que 0, 0 para sair): "))
    if n == 0:
        break
    if n > 0:
        soma += n
        quantidade += 1

if quantidade > 0:
    print(f"Quantidade: {quantidade}")
    print(f"Média: {soma / quantidade:.2f}")
else:
    print("Nenhum número válido foi digitado.")

