import allat

allatfajok = []

for _ in range(3):
    fajnev = input("Add meg egy állatfaj nevét! ")
    tomeg = input("Hány kilogramm a tömege egy példánynak? ")
    allatfaj = allat.Allatfaj(fajnev, tomeg)
    allatfajok.append(allatfaj)

legnehezebb_allat = allatfajok[0]

for allatfaj in allatfajok:
    print("A(z)", allatfaj.fajnev, "tömege", allatfaj.tomeg, "kg.", sep="")
    if allatfaj.tomeg > legnehezebb_allat.tomeg:
        legnehezebb_allat = allatfaj

with open("legnehezebb.txt", "w", encoding="utf-8") as celfajl:
    print("A(z)", legnehezebb_allat.fajnev, "a legnehezebb.", file=celfajl)