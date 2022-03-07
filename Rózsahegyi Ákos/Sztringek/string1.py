ss = "Hello világ"
tt = ss.upper()
print(tt)

gyumolcs = "banán"
lista = list(enumerate(gyumolcs))
print(lista)

primek = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
p4 = primek[4]
print(p4)

baratok = ["Misi","Petra","Botond","Jani","Csilla","Peti","Norbi"]
b3 = baratok[3]
print(b3)

gyumolcs = "banán"
hossz = len(gyumolcs)
print(hossz)

sz = len(gyumolcs)
utolso = gyumolcs[sz-1]
print(utolso)

i = 0
while i < len(gyumolcs):
    karakter = gyumolcs[i]
    print(karakter)
    i += 1
# vagy
for c in gyumolcs:
    print(c)