from turtle import Turtle, Screen
import random

donatello = Turtle()
scr = Screen()

# ##rectangles
# scr.colormode(255)
# for i in range (3, 11):
#     donatello.width(random.randint(1, 20))
#     donatello.pencolor(random.randint(1, 250), random.randint(1, 250), random.randint(1, 250))
#     for q in range (i):
#         donatello.right(360/i)
#         donatello.forward(100)

# ##random walk
# angles = [0, 90, 180, 270]
# scr.colormode(255)
# # donatello.hideturtle()
# donatello.width(20)
# donatello.speed(0)
# scr.setup (width=1800, height=1000)
# for i in range (1, 200):
#     donatello.pencolor(random.randint(1, 250), random.randint(1, 250), random.randint(1, 250))
#     donatello.setheading(random.choice(angles))
#     donatello.forward(30)

# ##Spirograph
donatello.speed(0)
scr.colormode(255)
donatello.width(5)
for i in range (1, 150):
    donatello.pencolor(random.randint(1, 250), random.randint(1, 250), random.randint(1, 250))
    donatello.circle(100)
    donatello.right(5)


scr.exitonclick()

