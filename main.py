from turtle import Screen

from paddle1 import Paddle

from paddle2 import Paddle_2

from Ball import Ball

from Barrier import Barrier

from Score import Score

import time

screen= Screen()

screen.setup(1000,800)

screen.bgcolor("black")

screen.title("!!!!!  Welcome To Pong Game Arena  !!!!")

screen.tracer(0)

ball= Ball()

paddle1=Paddle()

paddle2=Paddle_2()

barrier=Barrier()

score=Score()


game_on=True

screen.listen()

screen.onkey(paddle1.up,"Up")

screen.onkey(paddle1.down,"Down")

screen.onkey(paddle2.up,"w")

screen.onkey(paddle2.down,"s")

while game_on:

    screen.update()

    ball.move()


    time.sleep(0.1)


    if ball.ycor()>380 or ball.ycor()<-380:

        ball.bounce_y()

    if (ball.distance(paddle1)<60 and ball.xcor()>455) or (ball.distance(paddle2)<60 and ball.xcor()<-455):

        ball.bounce_x()

    if ball.xcor()>480:

        ball.reset_position()

        score.l_increase()

    if ball.xcor()<-480:

        ball.reset_position()

        score.r_increase()

    if paddle1.ycor()<-390:

        paddle1.paddle_down()

    if paddle1.ycor()>390:

        paddle1.paddle_up()

    

    if ball.xcor()<-480:

        ball.reset_position()

        score.r_increase()

    if paddle2.ycor()<-390:

        paddle2.paddle_down()

    if paddle2.ycor()>390:

        paddle2.paddle_up()

    
        


    



    

    

    

 

    

    
        
        

          

    
        
            














































screen.exitonclick()