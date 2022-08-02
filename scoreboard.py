from tkinter import font
from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.r_score=0
        self.l_score=0
        self.update()
    def update(self):
        self.goto(-100,200)
        self.write(self.l_score,align="center",font=("courier",80,'normal'))
        self.goto(100,200)
        self.write(self.r_score,align="center",font=("courier",80,'normal'))
    def l_point(self):
        self.clear()
        self.l_score+=1
        self.update()
    def r_point(self):
        self.clear()
        self.r_score+=1
        self.update() 