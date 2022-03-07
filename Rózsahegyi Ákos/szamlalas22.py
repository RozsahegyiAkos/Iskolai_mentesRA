szavak = ["Elemér", "Emma", "ajtó", "róka", "egér"]
darab = 0

for szo in szavak:
    if szo[0] == "e" or szo[0] == "E":
        print(szo)
        darab = darab + 1

print("*E* vagy *e* betűvel kezdődő szavak száma:", darab)