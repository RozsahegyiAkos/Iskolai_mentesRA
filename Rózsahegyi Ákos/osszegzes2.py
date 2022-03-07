szam = int(input("Adj meg egy számot -5 és 5 között! "))
osszeg = 0
list = []

while -5 <= szam <= 5:
    osszeg = osszeg + szam
    list.append(szam)
    szam = int(input("Adj meg még egy számot -5 és 5 között! "))
print(list)
print("Összeg: ", osszeg)