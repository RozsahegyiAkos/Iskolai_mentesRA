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


a = ablak_keszites("lightgreen", "Kockás spirál")
Zsolt = teknoc_keszites("Blue", 3, 10)
sz = 0
for i in range(100):
    Zsolt.forward(sz)
    Zsolt.right(89)
    sz = sz + 5
a.mainloop()