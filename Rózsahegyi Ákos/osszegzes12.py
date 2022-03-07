import random
list = []
osszeg = 0

for i in range(5):
    randszam = random.randint(1,10)
    list.append(randszam)
    if randszam % 2 == 0:
        osszeg = osszeg + randszam

print("A lista elemei:", list)
print("Az összeg:", osszeg)