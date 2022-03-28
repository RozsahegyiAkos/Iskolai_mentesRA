nyelvek = []
with open("prognyelvek.csv", "r", encoding="utf-8") as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(",")
        nyelv = {"evszam": int(adatok[0]), "programnyelv": adatok[1], "nev": adatok[2],  "feltalalo": adatok[3]}
        nyelvek.append(nyelv)

print(f"{nyelvek=}")