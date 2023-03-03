from turtle import Turtle, Screen


tim = Turtle()

# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(111)
# timmy_the_turtle.right(78) # in degree

for _ in range(3):
    """Paint a triangle"""
    tim.forward(100)
    tim.left(120)

tim.penup()
tim.forward(200)
tim.pendown()


for _ in range(6):
    """Paint a hexagon"""
    tim.forward(100)
    tim.left(60)





screen = Screen()
screen.exitonclick()
