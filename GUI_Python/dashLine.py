from turtle import Turtle,Screen


nemo_turtle = Turtle()
nemo_turtle.shape("turtle")
nemo_turtle.color("blue")


for num in range(15):
    nemo_turtle.forward(10)
    nemo_turtle.penup()
    nemo_turtle.forward(10)
    nemo_turtle.pendown()

















screen=Screen()
screen.exitonclick()