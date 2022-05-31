class Hiresno:
    def __init__(self, nev, foglalkozas, nemzetiseg):
        self.nev = nev
        self.foglalkozas = foglalkozas
        self.nemzetiseg = nemzetiseg
        
    def elotag(self):
        if self.nemzetiseg == "a":
            return "Ms."
        else:
            return "Frau"

hires_nok = []
for _ in range(3):
    nev = input("Add meg egy híres nő nevét! ")
    foglalkozas = input("Add meg a foglalkozását! ")
    nemzetiseg = input("Add meg a nemzetiségét (a/n)! ")
    hires_no = Hiresno(nev, foglalkozas, nemzetiseg)
    hires_nok.append(hires_no)

for hires_no in hires_nok:
    print(Hiresno.elotag(), hires_no.nev, "egy híres", hires_no.foglalkozas)