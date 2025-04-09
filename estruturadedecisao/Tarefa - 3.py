sexo = 0

sexo = input("Informe F para Feminino ou M para Masculino: ")

if (sexo.upper() == "M"):
    print("MASCULINO")
elif (sexo.upper() == "F"):
    print("FEMININO")
else:
    print("Sexo Invalido")