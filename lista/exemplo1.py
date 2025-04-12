frutas = ["maçã", "banana", "morango"]

for fruta in frutas:
    print(fruta)

print("")
frutas.append("Abacaxi")

for fruta in frutas:
    print(fruta)

frutas_copia = frutas.copy()

frutas.clear()

for fruta in frutas_copia:
    print(fruta)