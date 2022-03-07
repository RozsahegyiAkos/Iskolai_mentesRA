class Negyzet:
    def __init__(self, oldalhossz):
        self.oldalhossz = oldalhossz
    
    def terulet(self):
        return self.oldalhossz * self.oldalhossz
    
    def kerulet(self):
        return self.oldalhossz * 4
    
    def info(self):
        print(f"A(z) {self.oldalhossz} oldalhosszúságú négyzet területe {self.terulet()} egység, kerülete {self.kerulet()} egység")
    
'''
# Házi feladat verzió
oldalhosszak = []
adatbekeres = int(input("Adj meg egy oldalhosszat: "))

oldalhosszak.append(adatbekeres)
index = 0

while adatbekeres != 0:
    adatbekeres = int(input("Adj meg egy oldalhosszat: "))
    oldalhosszak.append(adatbekeres)

    if adatbekeres == 0:
        for oldal in oldalhosszak:
            negyzet = Negyzet(oldalhosszak[index])
            index += 1
            negyzet.info()
'''

# Helyes megoldás
negyzetek = []
adatbekeres = int(input("Adj meg egy oldalhosszat: "))

while adatbekeres != 0:
    negyzet = Negyzet(adatbekeres)
    negyzetek.append(negyzet)
    adatbekeres = int(input("Adj meg egy oldalhosszat: "))

# for i in range(len(negyzetek)):
    # print(negyzetek.info())

for negyzet in negyzetek:
    print(negyzet.info())

    

# negyzet_01 = Negyzet(3)
# print(negyzet_01.info())
# print("A négyzet területe:", negyzet_01.terulet())
# print("A négyzet kerülete:", negyzet_01.kerulet())