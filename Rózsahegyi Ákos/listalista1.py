import random
tarolo = []

for i in range(4):
    sor = []
    for i in range(3):
        randszam = random.randint(0,25)
        sor.append(randszam)
    tarolo.append(sor)

print(tarolo)