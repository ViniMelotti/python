altura = float(input("digite sua altura "))
sexo = int(input("digite 1 para feminino e 2 para masculino "))

if sexo == 1:
    peso = (72.7*altura)-58
    print(f"{peso} é o seu peso ideal ")
else:
    peso = (62.1*altura)-44.7
    print("%.3fkg é o seu peso ideal " %(peso))