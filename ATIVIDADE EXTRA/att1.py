total = 0
quantidade = 0

while True:
    preco = float(input("Digite o preço do produto (0 para encerrar): "))
    if preco == 0:
        break
    total += preco
    quantidade += 1

if quantidade > 0:
    media = total / quantidade
    print(f"\nTotal de produtos: {quantidade}")
    print(f"Valor total da compra: R$ {total:.2f}")
    print(f"Valor médio por produto: R$ {media:.2f}")
else:
    print("Nenhum produto foi registrado.")
