import turtle

def ablak_keszites(szin, ablaknev):
    a = turtle.Screen()
    a.bgcolor(szin)
    a.title(ablaknev)
    return a

def teknoc_keszites(szin, tm, s):
    t = turtle.Turtle()
    t.color(szin)
    t.pensize(tm)
    t.speed(s)
    return t

def csillag(sz, r):
    for i in range(5):
        Eszti.forward(sz)
        Eszti.right(r)

a = ablak_keszites("lightgreen", "Kockás spirál")
Eszti = teknoc_keszites("Purple", 3, 10)
for v in range(1):
    csillag(100, 144)
a.mainloop()