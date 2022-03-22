def kereses(szoveg, k):
    i = 0
    while i < len(szoveg):
        if szoveg[i] == k:
             return i
        i += 1
    return -1

print(kereses("Informatika", "o")) # 3
print(kereses("Informatika", "I")) # 0
print(kereses("Informatika", "a")) # 6
print(kereses("Informatika", "x")) # hiba

sz = "Tessék dolgozni!"
print(sz.find("e"))