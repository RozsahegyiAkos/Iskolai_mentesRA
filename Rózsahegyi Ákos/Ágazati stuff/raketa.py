bekeres = int(input("Hány órás visszaszámlálást tervezünk? "))
ora = bekeres
felfuggesztesek = 0

for i in range(ora, 0, -1):
    print("Visszaszámlálás:", i)
    valasz = input("Fel kell függeszteni a visszaszámlálást (i/n)? ")
    
    if valasz == "i":
        felfuggesztesek += 1

print("A rakéta a visszaszámlálást követően ennyi órával indult:", ora + felfuggesztesek)