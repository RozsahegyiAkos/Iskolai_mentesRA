lista = []

for i in range(5):
    szam = int(input("Adj meg egy számot! "))
    lista.append(szam)

min = lista[0]
max = lista[0]
for i in lista:
    if i < min:
        min = i
    if i > max:
        max = i

print("A legkisebb szám a listában:", min)
print("A legnagyobb szám a listában:", max)