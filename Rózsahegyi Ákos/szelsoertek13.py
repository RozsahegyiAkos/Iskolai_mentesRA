lista = []
lista2 = []

for i in range(10):
    szam = int(input("Adj meg egy számot! "))
    lista.append(szam)

for i in lista:
    if i % 2 == 0:
        lista.append(i)

min = lista[0]
max = lista[0]
for i in lista2:
    if i < min:
        min = i
    if i > max:
        max = i

print(lista2)
print("A legkisebb szám a listában:", min)
print("A legnagyobb szám a listában:", max)