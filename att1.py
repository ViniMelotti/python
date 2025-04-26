
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))


idade = ano_atual - ano_nascimento
print(f"Você tem {idade} anos.")


if idade >= 18:
    nome = input("Digite seu nome: ")
    print(f"{nome}, sua entrada foi permitida.")
else:
    print("Desculpe, sua entrada não é permitida.")