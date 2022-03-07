import random
list = []
darab = 0

for i in range(5):
    randszam = random.randint(1,10)
    list.append(randszam)
print("A lista elemei:", list)

for szam in list:
    if szam % 2 == 0:
        darab = darab + 1

print("A listában lévő kettővel osztható számok száma:", darab)