import json

with open("pelda.json", encoding="utf-8") as diak_adatok:
    adatok = json.load(diak_adatok)

print(type(adatok))
for diak in adatok["diakok"]:
    diak["osztaly"] = "10.B"
    print(diak)

with open("diakok2.json", "w", encoding="utf-8") as diak_adatok2:
    json.dump(adatok, diak_adatok2, indent=2)