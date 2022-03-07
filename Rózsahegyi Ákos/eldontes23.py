szo = "turhajó"
betu2 = input("Adj meg egy betűt! ")
talalat = False
index = 0
folytatja = True

while index < len(szo) and not talalat:
    if szo[index] == betu2:
        talalat = True
    index = index + 1
print("A szó:", szo)

while folytatja:
    valasz = input("Adj meg még egy betűt! ")
    if valasz == "":
        folytatja = False

if talalat:
    print("A kapott betű szerepel a szóban.")
else:
    print("A kapott betű nem szerepel a szóban.")