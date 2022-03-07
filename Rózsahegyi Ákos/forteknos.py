import turtle
ablak = turtle.Screen()
Sanyi = turtle.Turtle()
Sanyi.speed(1)
Sanyi.shape("circle")

#for sz in ["yellow", "red", "purple", "blue"]:
#Sanyi.color(sz)
#Sanyi.forward(50)
#Sanyi.left(90)

szinek = ["yellow", "red", "purple", "blue"]
for sz in szinek:
    Sanyi.color(sz)
    Sanyi.forward(50)
    Sanyi.left(90)

Sanyi.penup()
Sanyi.forward(120)
Sanyi.pendown()

szinek2 = ["yellow", "red", "purple", "blue"]
for sz2 in szinek2:
    Sanyi.color(sz2)
    Sanyi.forward(50)
    Sanyi.left(90)

ablak.mainloop()