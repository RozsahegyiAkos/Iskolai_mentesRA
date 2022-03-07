import random
list = []

for i in range(5):
    randszam = random.randint(1,10)
    list.append(randszam)
print("A lista elemei:", list)

osszeg = 0
for eredmeny in list:
    osszeg = osszeg + eredmeny
print("Az összes érték összege:", osszeg)