def a_betuk_szama(szoveg):
    darab = 0
    for k in szoveg:
        if k == "a":
            darab += 1
    return darab

print(a_betuk_szama("banán"))