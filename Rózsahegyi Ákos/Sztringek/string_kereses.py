def kereses(szoveg, k):
    i = 0
    while i < len(szoveg):
        if szoveg[i] == k:
             return i
        i += 1
    return -1

print(kereses("Informatika", "o"))
print(kereses("Informatika", "I"))
print(kereses("Informatika", "a"))
print(kereses("Informatika", "x"))
