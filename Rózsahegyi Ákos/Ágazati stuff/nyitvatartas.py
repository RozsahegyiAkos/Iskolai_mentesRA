bekeres = int(input("Hány óra van most? "))

if bekeres >= 8 and bekeres < 16:
    print("A bolt nyitva van.")
    print("Ennyi órád van még odaérni:", 16-bekeres)
else:
    print("A bolt zárva van.")