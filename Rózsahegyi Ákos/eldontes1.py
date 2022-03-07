import random
list = []
talalat = False
szam2 = int(input("Adj meg egy számot 1 és 7 között! "))

for i in range(5):
    randszam = random.randint(1,7)
    list.append(randszam)
print(list)

index = 0
while index < len(list) and not talalat:
    if list[index] == szam2:
        talalat = True
    index = index + 1
    
if talalat:
    print("Szerepel a listában a szám.")
else:
    print("Nem szerepel a listában a szám.")