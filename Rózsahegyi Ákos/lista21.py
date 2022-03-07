szavak = []
szo = None

while szo !="":
    szo = input("Adj meg kis a betűvel kezdődő szavakat! A szavakat listába mentem és kiírom ")
    if szo != "" and szo[0] == "a":
        szavak.append(szo)

print(szavak)