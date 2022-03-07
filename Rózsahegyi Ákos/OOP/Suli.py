import datetime

class Szemely:
    def __init__(self, nev):
        self.nev = nev
    
    def bemutatkozik(self):
        print(f"Szia, a nevem {self.nev},", end="")

class Diak(Szemely):
    def __init__(self, nev, osztaly):
        super().__init__(nev)
        self.osztaly = osztaly
    
    def bemutatkozik(self):
        super().bemutatkozik()
        print(f" és a(z) {self.osztaly} osztályba járok.")

class Tanar(Szemely):
    def __init__(self, nev, szakok):
        super().__init__(nev)
        self.szakok = szakok
    
    def bemutatkozik(self):
        super().bemutatkozik()
        print("", "-".join(self.szakok), "szakos tanár vagyok.")

diak_01 = Diak("Kiss Péter", "10.A")
tanar_01 = Tanar("Horváth Zita", ["biológia", "kémia"])
tanar_02 = Tanar("Schmidt Emil", ["matematika"])

diak_01.bemutatkozik()
tanar_01.bemutatkozik()
tanar_02.bemutatkozik()