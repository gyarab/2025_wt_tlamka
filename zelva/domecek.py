import turtle
from math import sqrt  
from random import randint

turtle.bgcolor("black")
turtle.title("Věčný návrat želvy")

t = turtle.Turtle()
t.shape("classic") 
t.pensize(2)
t.pencolor("white")
t.penup()
t.goto(-60, 150)
t.pendown()

def domecek(a):
    d = a * sqrt(2)
    s = d / 2
    # spodní hrana
    t.forward(a)
    # prava
    t.left(90)
    t.forward(a)
    # strecha
    t.left(45)
    t.forward(s)
    t.left(90)
    t.forward(s)
    # leva 
    t.left(45)
    t.forward(a)
    # křížem krážem
    t.left(135)
    t.forward(d)
    t.left(135)
    t.forward(a)
    t.left(135)
    t.forward(d)
    # konec
    t.left(45)

def zemekoule(pocet, velikost):                
        for i in range(pocet):
            domecek(velikost)
            t.right(360 / pocet)


zemekoule(12, randint(30, 70))

t.hideturtle()
t.penup()
t.pencolor("#FF8C00")

y = -160
t.goto(0, y)
t.write("„Tento život... budeš muset žít ještě jednou",
        align="center", font=("Arial", 14, "italic"))
t.goto(0, y - 30)
t.write("a ještě nesčíslněkrát...“",
        align="center", font=("Arial", 14, "italic"))
t.goto(0, y - 80)
t.write("- Friedrich Nietzsche",
        align="center", font=("Arial", 12, "bold"))

turtle.exitonclick()
