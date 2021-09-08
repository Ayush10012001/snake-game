from turtle import Turtle

snakebody = [(0, 0), (-20, 0), (-40, 0)]
up1 = 90
down1 = 270
left1 = 180
right1 = 0

class Snake:
    def __init__(self):
        self.addturtle = []
        self.createsnake()
        self.head=self.addturtle[0]

    def createsnake(self):
        for i in snakebody:    #adding inital body (size3)
            self.addsegements(i)

    def addsegements(self, position):    #adding obj(body of snake)
            tim = Turtle(shape="square")
            tim.color("white")
            tim.penup()
            tim.goto(position)
            self.addturtle.append(tim)

    def extend1(self):    #extending body as snake touches food
        self.addsegements(self.addturtle[-1].position())

    def movesnake(self):
        for seg in range(len(self.addturtle) - 1, 0, -1):
            newx = self.addturtle[seg - 1].xcor()
            newy = self.addturtle[seg - 1].ycor()

            self.addturtle[seg].goto(newx, newy)
        self.head.forward(20)



    def up(self):
        if self.head.heading() != down1:
            self.head.setheading(up1)

    def down(self):
        if self.head.heading() != up1:
            self.head.setheading(down1)
    def left(self):
        if self.head.heading() != right1:
            self.head.setheading(left1)
    def right(self):
        if self.head.heading() != left1:
            self.head.setheading(right1)
