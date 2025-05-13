valor_divida = float(input("Digite o valor da dívida: R$ "))
tabela_juros = [
    (1, 0),
    (3, 10),
    (6, 15),
    (9, 20),
    (12, 25)
]
print("\nValor da Dívida\tValor dos Juros\tQuantidade de Parcelas\tValor da Parcela")
for parcelas, juros in tabela_juros:
    valor_juros = (valor_divida * juros) / 100
    valor_total = valor_divida +  valor_juros
    valor_parcela = valor_total / parcelas
    print(f"R$ {valor_total:,.2f}\tR$ {valor_juros:,.2f}\t\t{parcelas}\t\t\tR$ {valor_parcela:,.2f}")
