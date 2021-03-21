import turtle as z
import time 
z.shape("arrow")
z.speed(5)
z.penup()
z.goto(-500, 275)
z.pendown()

z.color("white", "red")
z.begin_fill()
for n in range(2):
    z.forward(1000)
    z.right(90)
    z.forward(550)
    z.right(90)
z.end_fill()

z.penup()
z.goto(-50, 0)

z.penup()
z.backward(75)
z.left(90)
z.forward(125)
z.left(90)
z.pendown()

z.color("red", "white")
z.begin_fill()
z.circle(127.5)
z.end_fill()

z.penup()
z.goto(-87, 105.5)
z.pendown()

z.color("red", "red")
z.begin_fill()
z.circle(107)
z.end_fill()

z.penup()
z.color("red", "white")
z.goto(50, -35)
z.right(20)
z.begin_fill()
for x in range(5):
    z.forward(100)
    z.right(144)
z.end_fill()

z.penup()
z.goto(350, -255)
z.right(154)
z.color("white", "white")
z.write("Bünyamin Efe", font=("chiller", 14, 'normal', 'bold'))
z.goto(450, -350)
time.sleep(10)