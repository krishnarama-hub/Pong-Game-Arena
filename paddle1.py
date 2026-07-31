from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):

        super().__init__()

        self.shape("square")

        self.color("white")

        self.shapesize(stretch_len=1,stretch_wid=5)

        self.penup()

        self.goto(480,0)


    

    def up(self):

        self.y_cor=self.ycor()+40

        self.goto(self.xcor(),self.y_cor)

        

    def down(self):
        
        self.y_cor=self.ycor()-40

        self.goto(self.xcor(),self.y_cor)


    def paddle_up(self):

        self.goto(self.xcor(),self.ycor()-40)

    def paddle_down(self):

        self.goto(self.xcor(),self.ycor()+40)

        



