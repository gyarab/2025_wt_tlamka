import turtle
from math import sqrt
import time

turtle.bgcolor("#1a1a1a") 
turtle.title("Věčný návrat želvy")

t = turtle.Turtle()
t.shape("classic") 
t.pensize(2)
BARVA_DOMU = "#FFFFFF" 
BARVA_TEXTU = "#FF8C00" 

def domecek_jednim_tahem(a):
    uhlopricka = a * sqrt(2)
    strecha = (a * sqrt(2)) / 2

    # 1 Podlaha
    t.forward(a)
    # 2 Pravá stěna
    t.left(90)
    t.forward(a)
    # 3 Střecha pravá
    t.left(45)
    t.forward(strecha)
    # 4 Střecha levá
    t.left(90)
    t.forward(strecha)
    # 5 Levá stěna
    t.left(45)
    t.forward(a)
    # 6 Uhlopříčka nahoru
    t.left(135)
    t.forward(uhlopricka)
    # 7 Strop
    t.left(135)
    t.forward(a)
    # 8Uhlopříčka dolů
    t.left(135)
    t.forward(uhlopricka)
    
    t.left(45)

def zrozeni_iluze():
    t.showturtle()
    t.speed(3) 
    t.pencolor(BARVA_DOMU)
    t.pensize(3) 
    
    t.penup()
    t.goto(-100, -50) 
    t.pendown()

    domecek_jednim_tahem(200)
    
    time.sleep(1.0)

def prechod_do_reality():
    t.penup()
    t.clear() 
    t.goto(-40, 180) 
    t.setheading(0)
    time.sleep(0.5)

def planeta_vecneho_navratu(pocet_domu):
    t.speed(0)
    t.pencolor(BARVA_DOMU)
    t.pensize(2)
    velikost = 50
    uhel_otoceni = 360 / pocet_domu
    t.pendown()

    for _ in range(pocet_domu):
        domecek_jednim_tahem(velikost)
        t.right(uhel_otoceni)
def zjeveni_pravdy():
    t.hideturtle() 
    t.penup()
    t.pencolor(BARVA_TEXTU)

    y_start = -150 
    t.goto(0, y_start) 
    font_citatu = ("Georgia", 16, "italic")
    t.write("„Tento život... budeš muset žít ještě jednou", align="center", font=font_citatu)
    
    t.goto(0, y_start - 35)
    t.write("a ještě nespočetněkrát...“", align="center", font=font_citatu)

    t.goto(0, y_start - 100) 
    font_podpisu = ("Arial", 14, "bold")
    t.write("- Friedrich Nietzsche", align="center", font=font_podpisu)

zrozeni_iluze()
prechod_do_reality()
planeta_vecneho_navratu(12)
zjeveni_pravdy()
turtle.exitonclick()