szavak = []
szo = None

while szo !="":
    szo = input("Adj meg kis/nagy a betűvel kezdődő szavakat! A szavakat listába mentem és kiírom ")
    if szo != "" and (szo[0] == "a" or szo[0] == "A"):
        szavak.append(szo)

print(szavak)