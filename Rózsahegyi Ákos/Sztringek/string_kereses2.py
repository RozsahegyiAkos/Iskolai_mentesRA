def kereses2(szoveg, k, kezdet):
    i = kezdet
    while i < len(szoveg):
        if szoveg[i] == k:
            return i
        i += 1
    return -1

print(kereses2("banán", "n", 2))