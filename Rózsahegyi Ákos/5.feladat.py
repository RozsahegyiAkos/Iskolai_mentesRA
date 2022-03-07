folytatja = True
while folytatja:
    szam = int(input("Kérek egy számot ! "))
    if szam%2 == 0:
        folytatja = False
    elif szam%2 != 0:
        folytatja = True
        print("Ez nem páros szám! Kérlek adj meg egy új számot.")
print("Okés!")