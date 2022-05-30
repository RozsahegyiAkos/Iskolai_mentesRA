# Könnyű szintű feladat

bekeres1 = str(input("Adj meg egy szót! "))
szo1 = bekeres1
bekeres2 = str(input("Adj meg egy másik szót! "))
szo2 = bekeres2

if len(szo1) > len(szo2):
    print("A hosszabb szó:", szo1)
elif len(szo2) > len(szo1):
    print("A hosszabb szó:", szo2)
else:
    print("A két szó egyforma hosszú.")