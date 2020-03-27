import turtle


def draw_square(t, length):
    for i in range(4):
        t.forward(length)
        t.left(90)


wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Exercicio 1")
alex = turtle.Turtle()

for i in range(5):
    alex.penup()
    alex.setpos(-10*(i+1), -10*(i+1))
    alex.pendown()
    draw_square(alex, 20*(i+1))

alex.penup()
alex.setpos(-60, -60)

wn.mainloop()
