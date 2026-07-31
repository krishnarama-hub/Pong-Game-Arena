from turtle import Turtle

class Score(Turtle):

    def __init__(self):

        super().__init__()

        self.color("white")

        self.penup()

        self.hideturtle()

        self.l_score=0

        self.r_score=0

        self.score_board()


    def score_board(self):

        self.goto(-80,360)

        self.write(f"Score:{self.l_score}",align="center",font=("Arial",24,"normal"))

        self.goto(80,360)

        self.write(f"Score:{self.r_score}",align="center",font=("Arial",24,"normal"))

    def l_increase(self):

        self.clear()

        self.l_score+=1

        self.score_board()

    

    def r_increase(self):

        self.clear()

        self.r_score+=1

        self.score_board()

    
        

    
        



