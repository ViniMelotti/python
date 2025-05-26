palavra = input("Digite a palavra: ")
cont_vogal=0
cont_cons=0

for letra in palavra:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        cont_vogal += 1
    else:
        cont_cons += 1

print ("vc tem %s vogais" %(cont_vogal))
print ("vc tem %s consoantes" %(cont_cons))