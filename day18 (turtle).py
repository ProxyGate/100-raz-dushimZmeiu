from turtle import Turtle, Screen
import random
import colorgram


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

#==================================================================================================================================================================

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

#==================================================================================================================================================================

# ##Spirograph
# donatello.speed(0)
# scr.colormode(255)
# donatello.width(5)
# for i in range (1, 150):
#     donatello.pencolor(random.randint(1, 250), random.randint(1, 250), random.randint(1, 250))
#     donatello.circle(100)
#     donatello.right(5)

#==================================================================================================================================================================

## hirst painting
def shitshow(n):
    color = colorgram.extract(r"E:\Programs\1_PYcharm_projects\day 18 timmy\Hirst1.jpg", n)
    new_c_l = []
    for i in range (2, n):
        new_c = (color[i].rgb.r, color[i].rgb.g, color[i].rgb.b)
        new_c_l.append(new_c)
    return(new_c_l)

scr .colormode(255)
donatello.speed(0)
new_l = shitshow(25)
scr.setup (width=1600, height=1000)
donatello.penup()
donatello.goto(-250, -250)
donatello.pendown()
for n in range (-200, 300, 50):
    for i in range (10):
        donatello.color(random.choice(new_l))
        donatello.dot(20)
        donatello.penup()
        donatello.forward(50)
        donatello.pendown()
    donatello.penup()
    donatello.goto(-250, n)
    donatello.pendown()

    
scr.exitonclick()

#==================================================================================================================================================================

