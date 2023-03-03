import random
import turtle as t

tim = t.Turtle()

colours = ["DarkOrchid", "IndianRed", "wheat"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.color(random.choice(colours))
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    # you can add colour in here
    draw_shape(shape_side_n)
