from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score:{self.score}", align="center",font=("Arial",10,"normal"))
        self.hideturtle()

    def incscore(self):  #increase score
        self.score+=1
        self.clear()
        self.write(f"Score:{self.score}", align="center", font=("Arial", 10, "normal"))

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center", font=("Arial", 25, "normal"))
        self.goto(0,-40)
        self.write(f"Score:{self.score}", align="center", font=("Arial", 25, "normal"))