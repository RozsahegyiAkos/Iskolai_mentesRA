import turtle
ablak = turtle.Screen()
Sanyi = turtle.Turtle()
ablak.bgcolor("lightgreen")
Sanyi.shape("turtle")
Sanyi.color("blue")
Sanyi.pencolor("blue")

Sanyi.stamp

for ora in range(12):
    
    Sanyi.pendown()
    Sanyi.stamp
    Sanyi.penup()
    Sanyi.forward(60)
    Sanyi.pendown
    Sanyi.forward(20)
    Sanyi.penup()
    Sanyi.forward(20)
    Sanyi.stamp
    Sanyi.backward(100)
    Sanyi.right(30)
    Sanyi.pendown()
    Sanyi.stamp

ablak.mainloop()