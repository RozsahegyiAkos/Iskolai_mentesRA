# Könnyű szintű feladat

bekeres1 = int(input("Adj meg egy számot! "))
szam1 = bekeres1
bekeres2 = int(input("Adj meg egy másik számot! "))
szam2 = bekeres2

if szam1 > szam2:
    print("A nagyobb érték:", szam1)
elif szam2 > szam1:
    print("A nagyobb érték:", szam2)
else:
    print("A két szám egyenlő.")