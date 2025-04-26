numlado = int(input("digite numeros de lados "))
medida = int(input("digite a medida do lado em cm "))


if numlado < 3:
    print("não é um poligono")
else:
    if numlado == 3:
        area = ((medida*medida)*(3**(1/2)))/4
        print(f"é um triangulo com {area} de area ")
    else:
        if numlado == 4:
            area = medida*medida
            print(f"é um quadrado com {area} de area ")
        else:
            if numlado == 5:
                print("é um pentagono ")
            else:
                print("poligono não identificado")
