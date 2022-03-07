import random
poziciok = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
pozicio = random.choice(poziciok)
index = 0
talalat = False

valasztas = input("Adj meg egy pozíciót! (pl: A1) ")

while index <= 9 and not talalat:
    if pozicio == valasztas:
        talalat = True
    index = index + 1

    if talalat:
        print("A pozíció:", pozicio)
        print("Talált!")
        print("Ennyiből találtad ki:", index)
    else:
        print("Nem talált!")
        valasztas = input("Adj meg egy pozíciót! (pl: A1) ")