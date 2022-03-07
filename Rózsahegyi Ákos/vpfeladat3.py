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

def sokszog_rajzolas(t, n, sz):
    Eszti.forward(sz)
    Eszti.left(360/n)


a = ablak_keszites("lightgreen", "Sokszög")
Eszti = teknoc_keszites("hotpink", 5)
for i in range(8):
    sokszog_rajzolas(Eszti, 8, 50)
a.mainloop()