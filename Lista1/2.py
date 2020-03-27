import turtle


def draw_poly(t, n, sz):

    if n > 2:
        for i in range(n):
            t.forward(sz)
            t.left(360/n)


wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Exercicio 1")
alex = turtle.Turtle()

draw_poly(alex, 3, 50)

wn.mainloop()
