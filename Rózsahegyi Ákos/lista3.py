import random
szamlista = []

for x in range(10):
    szam = random.randint(0,50)
    if szam % 4 == 0:
        szamlista.append(szam)

print(szamlista)
print("A lista ", len(szamlista), "elemből áll.")