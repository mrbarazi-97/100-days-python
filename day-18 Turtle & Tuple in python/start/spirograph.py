import random
import turtle as t

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
# tim.speed(0) # it's true too


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


# for _ in range(72):
#     tim.color(random_color())
#     tim.circle(100)
#     current_heading = tim.heading()
#     tim.setheading(current_heading + 5)
#print(current_heading) # print position of heading in console


def draw_spirography(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(random.randint(80, 100))
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)


draw_spirography(10)

screen = t.Screen()
screen.exitonclick()