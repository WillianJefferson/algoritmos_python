preco_1 = 0
preco_2 = 0
preco_3 = 0
preco_1 = int(input("Informe o preco 1: "))
preco_2 = int(input("Informe o preco 2: "))
preco_3 = int(input("Informe o preco 3: "))

if (preco_1 == preco_2) and (preco_1 == preco_3):
    print("Pode comprar qualquer um por que os preços são iguais.")
elif (preco_1 < preco_2) and (preco_1 < preco_3):
    print("Compre pelo preço 1")
elif (preco_2 < preco_3):
    print("Compre pelo preço 2")
else:
    print("Compre pelo preço 3")