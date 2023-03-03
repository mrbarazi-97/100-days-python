import random
import turtle as t

t.colormode(255)

tim = t.Turtle()
tim.pensize(15)
direction = [0, 90, 180, 270]
tim.speed("fastest")
# tim.speed(0) # it's true too


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))

