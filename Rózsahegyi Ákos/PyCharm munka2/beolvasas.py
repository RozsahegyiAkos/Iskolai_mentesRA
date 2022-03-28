'''
forrasfajl = open("autok_listaja.csv")
forrasfajl.readline()
for sor in forrasfajl:
    print(sor)

forrasfajl.close()
'''

'''
autok = []
with open("autok_listaja.csv", "r", encoding="utf-8") as forrasfajl:
    for sor in forrasfajl:
        print(sor)
'''

autok = []
with open("autok_listaja.csv", "r", encoding="utf-8") as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(",")
        auto = {"rendszam": adatok[0], "tipus": adatok[1], "kor": int(adatok[2])}
        autok.append(auto)

print(f"{autok=}")