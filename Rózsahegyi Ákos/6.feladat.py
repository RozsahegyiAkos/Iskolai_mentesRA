from random import randint

szamlalo = 0
i = 0
while i < 20:
    ertek = randint(1,12)
    if ertek % 3 == 0:
        print(ertek)
        szamlalo +=1
    i += 1
print("Hárommal osztható szám ", szamlalo, " db volt.")