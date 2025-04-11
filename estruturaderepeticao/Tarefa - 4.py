pop_A = 80000
cre_A = 0.03
pop_B = 200000
cre_B = 0.015

ano = 0
while (pop_A <= pop_B):
    pop_A += pop_A * cre_A
    print("População A", pop_A)
    pop_B += pop_B * cre_B
    print("População B", pop_B)
    ano = ano + 1
    print("ano", ano)


print("Será nescessário ", ano)