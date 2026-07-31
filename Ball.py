from turtle import Turtle

class Ball(Turtle):

    def __init__(self):

        super().__init__()

        self.color("white")

        self.shape("circle")

        self.shapesize(stretch_len=0.5,stretch_wid=0.5)

        self.penup()

        self.x_cor=10

        self.y_cor=10

        self.ball=0.02

    def move(self):

        self.x_aixs=self.xcor()+self.x_cor

        self.y_aixs=self.ycor()+self.y_cor

        self.goto(self.x_aixs,self.y_aixs)
        
    def bounce_x(self):

        self.x_cor*=-1

    def bounce_y(self):

        self.y_cor*=-1

    def reset_position(self):

        self.goto(0,0)

    def speed(self):

        self.ball*=0.09