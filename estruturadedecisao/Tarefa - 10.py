turno = ""

print("-- Em que turno você estuda?")
print("Digite M para Matutino, V para Vespertino e N para Noturno")

turno = input("Opção escolhida: ").upper()

if (turno == "M"):
    print("Bom dia")
elif (turno == "V"):
    print("Boa tarde")
elif (turno == "N"):
    print("Boa noite")
else:
    print("Valor Invalido")