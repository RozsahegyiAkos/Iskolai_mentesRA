import turtle
ablak = turtle.Screen()
Sanyi = turtle.Turtle()

for harom in range(3):
    Sanyi.forward(80)
    Sanyi.left(120)

Sanyi.penup()
Sanyi.right(90)
Sanyi.forward(100)
Sanyi.left(90)
Sanyi.pendown()

for negy in range(4):
    Sanyi.forward(80)
    Sanyi.left(90)

Sanyi.penup()
Sanyi.right(90)
Sanyi.forward(150)
Sanyi.left(90)
Sanyi.pendown()

for hat in range(6):
    Sanyi.forward(60)
    Sanyi.left(60)

Sanyi.penup()
Sanyi.backward(200)
Sanyi.pendown()

for nyolc in range(8):
    Sanyi.forward(60)
    Sanyi.left(45)

ablak.mainloop()