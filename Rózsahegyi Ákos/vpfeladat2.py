import turtle

def ablak_keszites(szin, ablaknev):
    a = turtle.Screen()
    a.bgcolor(szin)
    a.title(ablaknev)
    return a

def teknoc_keszites(sz, tm):
    t = turtle.Turtle()
    t.color(sz)
    
    return t

def negyzetek(m):
    for i in range(4):
        Eszti.forward(m)
        Eszti.left(90)
    Eszti.penup()
    Eszti.backward(10)
    Eszti.right(90)
    Eszti.forward(10)
    Eszti.left(90)
    Eszti.pendown()


a = ablak_keszites("lightgreen", "Négyzetek")
Eszti = teknoc_keszites("hotpink", 5)
meret = 20
for i in range(5):
    negyzetek(meret)
    meret = meret + 20

a.mainloop()