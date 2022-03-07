import turtle
ablak = turtle.Screen()
szin = str(input("Adj meg háttérszínt: "))
ablak.bgcolor(szin)
ablak.title("Hello, Eszti!")

Eszti = turtle.Turtle()
Eszti.color("blue")
Eszti.pensize(3)

Eszti.forward(50)
Eszti.left(120)
Eszti.forward(50)

ablak.mainloop()
