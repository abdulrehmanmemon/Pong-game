from turtle import Turtle,Screen
from paddle_class import paddle
from scoreboard import Score
from ball import ball
import time
screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PONG GAME")
screen.tracer(0)
r_paddle=paddle(350,0)
l_paddle=paddle(-350,0)
bal=ball()
score=Score()
screen.listen()
screen.onkey(key="Up",fun=r_paddle.up)
screen.onkey(key='Down',fun=r_paddle.down)
screen.onkey(key="w",fun=l_paddle.up)
screen.onkey(key='s',fun=l_paddle.down)
game_is_on=True
t=0.1
while game_is_on:
    time.sleep(bal.move_speed)
    screen.update()
    bal.move()
    if bal.ycor()>290 or bal.ycor()<-290:
        bal.bounce_y()
    if bal.distance(r_paddle)<50 and bal.xcor()>320 or bal.distance(l_paddle)<50 and bal.xcor()<-320:
        bal.bounce_x()
    if bal.xcor()>380:
        bal.reset_position()
        score.l_point()
    if bal.xcor()<-380:
        bal.reset_position()
        score.r_point()
screen.exitonclick()