import turtle as turt
import random
turt.colormode(255)

def random_color():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)

    return (red, green, blue)


turtle = turt.Turtle()
turtle.speed("fastest")

def get_spirograph(angle_shift):

    for i in range (int(360/angle_shift)):
        color = random_color()
        turtle.pencolor(color)
        turtle.circle(100)
        turtle.left(angle_shift)
        turtle.fd(5) 

get_spirograph(5)

screen = turt.Screen()
screen.exitonclick()