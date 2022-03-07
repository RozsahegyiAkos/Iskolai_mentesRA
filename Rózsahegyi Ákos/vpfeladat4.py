import turtle

def ablak_keszites(szin, ablaknev):
    a = turtle.Screen()
    a.bgcolor(szin)
    a.title(ablaknev)
    return a

def teknoc_keszites(sz, tm, s):
    t = turtle.Turtle()
    t.color(sz)
    t.speed(s)
    
    return t

def gyonyoru_abra(h):
    for a in range(4):
        for i in range(3):
            Eszti.forward(h)
            Eszti.left(90)
        Eszti.forward(h)
    Eszti.left(90)
    Eszti.right(15)


a = ablak_keszites("lightgreen", "Gyönyörű minta")
Eszti = teknoc_keszites("hotpink", 5, 9)
for i in range(8):
    gyonyoru_abra(50)
a.mainloop()