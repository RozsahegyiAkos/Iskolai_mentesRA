szavak = ["alma", "barack", "Attila", "kávé", "szekrény", "asztal"]
darab = 0

for szo in szavak:
    if szo[0] == "a" or szo[0] == "A":
        print(szo)
        darab = darab + 1

print("*A* vagy *a* betűvel kezdődő szavak száma:", darab)