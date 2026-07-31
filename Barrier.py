from turtle import Turtle

class Barrier:

    def __init__(self):
        

        for y in range(-380, 381, 40):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.shapesize(stretch_wid=1, stretch_len=0.5)
            segment.goto(0, y)
            