szavak = []

for i in range(3):
    szo = input("Adj meg egy szót! ")
    szavak.append(szo)

min = szavak[0]

for i in szavak:
    if i < min:
        min = i


print("Legrövidebb", min)