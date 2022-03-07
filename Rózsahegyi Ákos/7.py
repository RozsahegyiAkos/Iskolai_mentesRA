import turtle
ablak = turtle.Screen()
Sanyi = turtle.Turtle()

for i in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    Sanyi.forward(100)
    Sanyi.right(i)

ablak.mainloop()