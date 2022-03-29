nyelvek = []
with open("prognyelvek.csv", "r", encoding="utf-8") as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(";")
        nyelv = {"evszam": int(adatok[0]), "nyelv": adatok[1], "feltalalo": adatok[2]}
        nyelvek.append(nyelv)

print(f"{nyelvek=}")